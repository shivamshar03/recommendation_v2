# embeddings/song_embedding.py

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # or OpenAI/Groq LLM via API

def generate_song_embedding(lyrics: str, genre: str, emotion: str):
    """
    Combines lyrics, genre, and emotion into a single vector.
    """
    combined_text = f"Genre: {genre}. Emotion: {emotion}. Lyrics: {lyrics}"
    return model.encode(combined_text)
