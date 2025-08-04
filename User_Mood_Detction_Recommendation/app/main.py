from .services.recommendation import generate_recommendations

from .config import config
from . import logger


def main():
    logger.info("🎵 Starting Real-Time Mood-Based Music Recommendation Engine...")

    # Step 1: Load user activity (mock or real-time)
    # Step 2: Run mood engine (LLM + Heuristic)
    # Step 3: Embed user mood
    # Step 4: Run FAISS search
    # Step 5: Filter, score, and rank songs
    # Step 6: Output recommendations

    recommendations = generate_recommendations(user_id="user_001")

    print("\n🎧 Top Recommendations:")
    for idx, rec in enumerate(recommendations, start=1):
        print(f"{idx}. {rec['title']} by {rec['artist']} [Score: {rec['score']:.2f}]")


if __name__ == "__main__":
    main()
