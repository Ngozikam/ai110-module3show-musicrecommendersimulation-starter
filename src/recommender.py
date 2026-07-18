from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numerical fields to numeric types."""

    import csv

    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Existing numerical attributes
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            # Advanced numerical attributes
            row["popularity"] = int(row["popularity"])
            row["release_decade"] = int(row["release_decade"])
            row["instrumentalness"] = float(row["instrumentalness"])
            row["speechiness"] = float(row["speechiness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a song's preference score using basic and advanced features."""

    score = 0.0
    reasons = []

    # Basic features

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    score += energy_similarity
    reasons.append(f"energy similarity (+{energy_similarity:.2f})")

    # Advanced features

    if song["detailed_mood"] == user_prefs["detailed_mood"]:
        score += 0.5
        reasons.append("detailed mood match (+0.5)")

    popularity_similarity = 1 - abs(
        song["popularity"] - user_prefs["popularity"]
    ) / 100
    score += 0.5 * popularity_similarity
    reasons.append(
        f"popularity similarity (+{0.5 * popularity_similarity:.2f})"
    )

    if song["release_decade"] == user_prefs["release_decade"]:
        score += 0.5
        reasons.append("release decade match (+0.5)")

    instrumentalness_similarity = 1 - abs(
        song["instrumentalness"] - user_prefs["instrumentalness"]
    )
    score += 0.5 * instrumentalness_similarity
    reasons.append(
        f"instrumentalness similarity (+{0.5 * instrumentalness_similarity:.2f})"
    )

    speechiness_similarity = 1 - abs(
        song["speechiness"] - user_prefs["speechiness"]
    )
    score += 0.5 * speechiness_similarity
    reasons.append(
        f"speechiness similarity (+{0.5 * speechiness_similarity:.2f})"
    )

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score and rank songs, returning the top k recommendations with explanations."""

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_songs[:k]



