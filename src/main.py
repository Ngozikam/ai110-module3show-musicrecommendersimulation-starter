"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "detailed_mood": "euphoric",
            "popularity": 90,
            "release_decade": 2020,
            "instrumentalness": 0.05,
            "speechiness": 0.08
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
            "detailed_mood": "serene",
            "popularity": 65,
            "release_decade": 2020,
            "instrumentalness": 0.75,
            "speechiness": 0.04
        },
        "Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "detailed_mood": "aggressive",
            "popularity": 85,
            "release_decade": 2010,
            "instrumentalness": 0.05,
            "speechiness": 0.09
        },
        "Conflicting Preferences": {
            "genre": "pop",
            "mood": "chill",
            "energy": 0.9,
            "detailed_mood": "calm",
            "popularity": 80,
            "release_decade": 2020,
            "instrumentalness": 0.50,
            "speechiness": 0.05
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        print(f"\n=== {profile_name} ===")
        print(
            f"Preferences: genre={user_prefs['genre']}, "
            f"mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']}"
        )

        recommendations = recommend_songs(
            user_prefs,
            songs,
            k=5
        )

        print("\nTop recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()