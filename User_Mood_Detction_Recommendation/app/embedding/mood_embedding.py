# embeddings/mood_embedding.py

from sentence_transformers import SentenceTransformer
import datetime

model = SentenceTransformer("all-MiniLM-L6-v2")  # Can be swapped with OpenAI/Groq API

def generate_mood_embedding(user_activity: dict):
    """
    Generates mood embedding using heuristics + textual representation.
    """
    timestamp = datetime.datetime.strptime(user_activity["timestamp"], "%Y-%m-%d %H:%M")
    time_category = "morning" if 5 <= timestamp.hour < 12 else \
                    "afternoon" if 12 <= timestamp.hour < 18 else \
                    "evening" if 18 <= timestamp.hour < 22 else "late night"

    # Heuristic summary
    text_summary = f"""
    Time: {time_category}. 
    Average replays: {user_activity['average_replays']}.
    Total skips: {user_activity['total_skips']}.
    Recent emotions: {', '.join([song['emotion'] for song in user_activity['recent_songs']])}.
    Genres: {', '.join(set([song['genre'] for song in user_activity['recent_songs']]))}.
    """

    return model.encode(text_summary)
