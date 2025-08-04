def compute_final_score(song, user_embedding, weight_config=None):
    """
    Combine multiple signals (similarity score, emotion match, replay score) into a final score.

    Args:
        song (dict): Song metadata including similarity, emotion_score, replay_rating.
        user_embedding (np.array): Embedding vector of user mood or preference.
        weight_config (dict): Optional weight settings.

    Returns:
        float: Final score.
    """
    if weight_config is None:
        weight_config = {
            'similarity': 0.5,
            'emotion_score': 0.3,
            'replay_rating': 0.2
        }

    similarity = song.get('similarity', 0)
    emotion_score = song.get('emotion_score', 0)
    replay_rating = song.get('replay_rating', 0)

    final_score = (
        weight_config['similarity'] * similarity +
        weight_config['emotion_score'] * emotion_score +
        weight_config['replay_rating'] * replay_rating
    )
    return final_score
