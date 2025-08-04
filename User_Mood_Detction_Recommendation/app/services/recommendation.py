# services/recommendation.py

import json
import pandas as pd
from ..mood_engine.hybrid import hybrid_mood_score
from ..embedding import generate_mood_embedding, generate_song_embedding
from ..vector_search.indexer import FAISSIndexer
from ..vector_search.search import FAISSSearcher
from ..filter_score import genre_replay_filter, compute_final_score
from ..models.recommendation_output import RecommendedSong
from ..config import config
import numpy as np


def load_user_activity(user_id):
    with open(config.USER_ACTIVITY_PATH, "r") as f:
        data = json.load(f)
    if data["user_id"] == user_id:
        return data
    return None


def load_song_db():
    return pd.read_csv(config.SONG_DB_PATH)


def generate_recommendations(user_id):
    user_activity = load_user_activity(user_id)
    if not user_activity:
        raise ValueError(f"No activity found for user {user_id}")

    # Mood detection
    recent_song = user_activity["recent_songs"][-1]
    mood_result = hybrid_mood_score(user_activity["recent_songs"], recent_song["title"])
    final_mood = mood_result["final_mood"]

    # Embedding
    user_embedding = generate_mood_embedding(user_activity)
    song_db = load_song_db()
    song_embeddings = []
    song_ids = []
    for _, row in song_db.iterrows():
        emb = generate_song_embedding(row["lyrics"], row["genre"], final_mood)
        song_embeddings.append(emb)
        song_ids.append(row["song_id"])

    song_embeddings = np.array(song_embeddings)
    print("User embedding shape:", user_embedding.shape)
    print("Song embeddings shape:", song_embeddings.shape)
    print("Song IDs used for indexing:", song_ids)

    # Vector search
    indexer = FAISSIndexer(dim=len(user_embedding))
    indexer.build_index(song_embeddings, song_ids)
    searcher = FAISSSearcher(indexer, top_k=config.TOP_K_RECOMMENDATIONS)
    results = searcher.search(np.array(user_embedding))

    # Filter and score
    recommended = []
    user_genres = list(set([s["genre"] for s in user_activity["recent_songs"]]))
    for res in results:
        song_match = song_db[song_db["song_id"] == res["metadata_id"]]
        if song_match.empty:
            print(f"Warning: No song found for metadata_id {res['metadata_id']}")
            continue  # Skip this result if no match found
        song_row = song_match.iloc[0]
        emotion_emb = song_row.get("emotion_embedding", "")
        # If it's a string, check for mood match; if it's a list, skip or handle differently
        if isinstance(emotion_emb, str):
            emotion_score = 1.0 if final_mood in emotion_emb else 0.5
        else:
            emotion_score = 0.5  # or compute similarity if you want

        song_dict = {
            "song_id": song_row["song_id"],
            "title": song_row["title"],
            "artist": song_row.get("artist", "Unknown"),
            "genre": song_row["genre"],
            "replay_rating": 1.0,  # Placeholder, can be computed
            "similarity": 1.0 - res["distance"],
            "emotion_score": emotion_score,
        }
        recommended.append(song_dict)

    print("Initial recommended candidates:", recommended)  # <--- Add here

    filtered = genre_replay_filter(recommended, user_genres)
    for song in filtered:
        song["score"] = compute_final_score(song, user_embedding)

    # Format output
    output = [
        RecommendedSong(
            song_id=s["song_id"],
            title=s["title"],
            artist=s["artist"],
            score=s["score"]
        ).dict()
        for s in sorted(filtered, key=lambda x: x["score"], reverse=True)
    ]

    return output
