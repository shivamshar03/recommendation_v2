# mood_engine/llm.py

from transformers import pipeline

# Load sentiment pipeline from HuggingFace
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def llm_mood_from_lyrics(lyrics):
    """
    Uses an LLM (sentiment classifier) to infer mood from song lyrics.

    Args:
        lyrics (str): Song lyrics or snippet.

    Returns:
        str: Predicted mood label.
    """
    result = sentiment_model(lyrics[:512])[0]
    label = result["label"].lower()

    if label == "positive":
        return "happy"
    elif label == "negative":
        return "sad"
    else:
        return "neutral"
