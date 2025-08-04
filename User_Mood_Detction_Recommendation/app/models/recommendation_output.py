from pydantic import BaseModel
from typing import List

class RecommendedSong(BaseModel):
    song_id: str
    title: str
    artist: str
    score: float  # Recommendation confidence or similarity score

class RecommendationOutput(BaseModel):
    user_id: str
    mood_state: str
    recommended_songs: List[RecommendedSong]
