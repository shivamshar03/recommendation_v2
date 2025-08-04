# mood_engine/formatter.py

def format_interaction_log(log):
    """
    Convert raw user interaction logs into a structured format.

    Args:
        log (dict): Example: {'song_id': 'abc123', 'action': 'like', 'timestamp': '2025-07-31 14:45'}

    Returns:
        dict: Formatted user activity.
    """
    return {
        "song_id": log.get("song_id"),
        "action": log.get("action"),
        "timestamp": log.get("timestamp")
    }
