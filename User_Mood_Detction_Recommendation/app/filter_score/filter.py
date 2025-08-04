def genre_replay_filter(recommended_songs, user_preferred_genres, min_replay_rating=1.0):
    """
    Filter recommended songs based on genre match and minimum replay rating.

    Args:
        recommended_songs (list of dict): Songs with metadata including genre and replay rating.
        user_preferred_genres (list): List of user's favorite genres.
        min_replay_rating (float): Minimum threshold of replay rating to retain a song.

    Returns:
        list of dict: Filtered songs.
    """
    filtered = []
    for song in recommended_songs:
        if song['genre'] in user_preferred_genres and song.get('replay_rating', 0) >= min_replay_rating:
            filtered.append(song)
    return filtered
