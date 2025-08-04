# mood_engine/heuristic.py

from ..utils.time_utils import get_time_of_day, is_recent

def infer_mood_from_interactions(interactions):
    """
    Infer basic mood using heuristic rules based on user actions.

    Args:
        interactions (list): List of user interaction dictionaries

    Returns:
        str: Heuristic-based mood tag (e.g. "energetic", "calm", "sad")
    """
    mood_scores = {"happy": 0, "sad": 0, "energetic": 0, "calm": 0}

    for i in interactions:
        action = i.get("action")
        time_of_day = get_time_of_day()

        if action == "like":
            mood_scores["happy"] += 2
            if time_of_day == "morning":
                mood_scores["energetic"] += 1
        elif action == "skip":
            mood_scores["sad"] += 1
        elif action == "play":
            mood_scores["calm"] += 1

    return max(mood_scores, key=mood_scores.get)
