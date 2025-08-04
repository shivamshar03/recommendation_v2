from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SongInteraction(BaseModel):
    genre: str
    emotion: str
    liked: bool
    skipped: int
    duration: float  # in minutes

class UserActivity(BaseModel):
    timestamp: datetime
    recent_songs: List[SongInteraction]
    average_replays: float
    total_skips: int
