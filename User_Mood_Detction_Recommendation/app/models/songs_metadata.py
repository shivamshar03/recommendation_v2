from pydantic import BaseModel
from typing import List

class SongMetadata(BaseModel):
    song_id: str
    title: str
    artist: str
    genre: str
    lyrics: str
    emotion_tags: List[str]
    embedding: List[float]
