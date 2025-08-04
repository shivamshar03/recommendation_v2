
```
music_recommender/
├── app/
│   ├── __init__.py
│   ├── main.py                        # Entry point (FastAPI / Streamlit / CLI)
│   ├── config.py                      # Configuration, API keys, constants
│
│   ├── models/                        # 📦 Data Schemas & Representations
│   │   ├── __init__.py
│   │   ├── user_activity.py           # User interaction data
│   │   ├── song_metadata.py           # Song features, lyrics, genre, emotion
│   │   └── recommendation_output.py   # Output recommendation format
│
│   ├── interaction/                   # 🎮 User Activity Capture
│   │   ├── __init__.py
│   │   └── collector.py               # Capture play, like, skip, timestamps
│
│   ├── mood_engine/                   # 🧠 Real-Time Mood Engine (LLM + Heuristic)
│   │   ├── __init__.py
│   │   ├── formatter.py               # Format data for LLM
│   │   ├── heuristic.py               # Rule-based mood detection
│   │   ├── llm.py                     # LLM-based emotion analysis
│   │   └── hybrid.py                  # Combine heuristic + LLM
│
│   ├── embedding/                     # 💫 Embedding Generation
│   │   ├── __init__.py
│   │   ├── mood_embedding.py          # Generate LLM/BERT embedding for user
│   │   └── song_embedding.py          # Embed lyrics + metadata of songs
│
│   ├── vector_search/                 # 🔍 FAISS Similarity Search
│   │   ├── __init__.py
│   │   ├── indexer.py                 # Build & maintain FAISS index
│   │   └── search.py                  # Query songs similar to user mood
│
│   ├── filter_score/                  # 🎯 Filter & Final Scoring
│   │   ├── __init__.py
│   │   ├── filter.py                  # Genre, replay rating, recentness
│   │   └── scorer.py                  # Weighted multi-source scoring
│
│   ├── services/                      # 🔌 Service Orchestration
│   │   ├── __init__.py
│   │   └── recommendation.py         # Full pipeline wrapper
│
│   ├── utils/                         # ⚙️ Utility Tools
│   │   ├── __init__.py
│   │   ├── logger.py                  # Logging
│   │   └── time_utils.py              # Time-of-day, recent activity handling
│
│   └── data/                          # 📂 Sample Data
│       ├── sample_user_activity.json
│       └── sample_song_db.csv
│
├── requirements.txt
├── README.md
└── .env                               # Keys for OpenAI, Groq, etc.
```