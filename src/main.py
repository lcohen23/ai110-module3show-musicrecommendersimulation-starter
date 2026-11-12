"""
Command line runner for the Music Recommender Simulation.

Run with: python -m src.main
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    """Load the catalog, score it for the default profile, and print the top picks."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    print(
        f"\nProfile: genre={user_prefs['favorite_genre']}, mood={user_prefs['favorite_mood']}, "
        f"energy={user_prefs['target_energy']}, likes_acoustic={user_prefs['likes_acoustic']}"
    )
    print("\nTop recommendations:\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} by {song['artist']}  [{score:.2f} / 5.00]")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print()


if __name__ == "__main__":
    main()
