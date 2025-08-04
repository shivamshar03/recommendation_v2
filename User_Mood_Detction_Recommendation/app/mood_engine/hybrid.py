# mood_engine/hybrid.py

from .heuristic import infer_mood_from_interactions
from .llm import llm_mood_from_lyrics

def hybrid_mood_score(interactions, lyrics):
    """
    Combine LLM + heuristic predictions to generate a final mood label.

    Args:
        interactions (list): User activity list
        lyrics (str): Current/most played song lyrics

    Returns:
        dict: Final mood engine output
    """
    heuristic_mood = infer_mood_from_interactions(interactions)
    llm_mood = llm_mood_from_lyrics(lyrics)

    if heuristic_mood == llm_mood:
        final = heuristic_mood
    else:
        # Weighted logic, LLM has more influence if user interaction is older
        final = llm_mood

    return {
        "heuristic": heuristic_mood,
        "llm": llm_mood,
        "final_mood": final
    }
