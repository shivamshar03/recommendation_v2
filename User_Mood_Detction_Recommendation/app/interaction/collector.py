# interaction/collector.py

from datetime import datetime
from typing import Dict, List, Optional


class UserInteractionCollector:
    def __init__(self):
        self.user_logs: Dict[str, List[Dict]] = {}

    def log_event(
        self,
        user_id: str,
        song_id: str,
        action: str,  # e.g., "play", "like", "skip"
        timestamp: Optional[str] = None,
        genre: Optional[str] = None,
    ):
        """
        Logs a user interaction event.

        Args:
            user_id (str): Unique identifier for the user.
            song_id (str): ID of the song involved in the interaction.
            action (str): One of ["play", "like", "skip"].
            timestamp (str, optional): ISO timestamp. If None, current time is used.
            genre (str, optional): Genre of the song (if available).
        """
        if action not in {"play", "like", "skip"}:
            raise ValueError("Invalid action type. Must be play, like, or skip.")

        if user_id not in self.user_logs:
            self.user_logs[user_id] = []

        self.user_logs[user_id].append({
            "song_id": song_id,
            "action": action,
            "timestamp": timestamp or datetime.utcnow().isoformat(),
            "genre": genre,
        })

    def get_recent_activity(self, user_id: str, within_days: int = 7) -> List[Dict]:
        """
        Returns recent activity for a user within the last `within_days` days.
        """
        now = datetime.utcnow()
        cutoff = now.timestamp() - within_days * 86400  # days to seconds

        return [
            event for event in self.user_logs.get(user_id, [])
            if datetime.fromisoformat(event["timestamp"]).timestamp() >= cutoff
        ]

    def get_last_action(self, user_id: str) -> Optional[Dict]:
        """
        Get the most recent action of the user.
        """
        return self.user_logs.get(user_id, [])[-1] if user_id in self.user_logs else None
