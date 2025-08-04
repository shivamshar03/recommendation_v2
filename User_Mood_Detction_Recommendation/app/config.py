# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Paths
    SONG_DB_PATH = os.path.join(BASE_DIR, "app", "data", "sample_song_db.csv")
    USER_ACTIVITY_PATH = os.path.join(BASE_DIR, "app", "data", "sample_user_activity.json")
    FAISS_INDEX_PATH = os.path.join(BASE_DIR, "app", "vector_search", "faiss_index")

    # LLM Parameters
    LLM_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 512

    # Heuristic Weights
    MOOD_WEIGHT = 0.4
    GENRE_WEIGHT = 0.3
    REPLAY_WEIGHT = 0.3

    # Embedding Models
    SONG_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    MOOD_EMBED_MODEL = "bert-base-uncased"

    # Other
    RECENT_DAYS_THRESHOLD = 3     # To treat activity as recent
    TOP_K_RECOMMENDATIONS = 10    # Number of final recommendations

config = Config()
