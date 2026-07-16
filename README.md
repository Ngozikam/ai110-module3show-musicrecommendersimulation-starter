# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple content-based music recommender in Python. It compares song features with a user's taste profile, calculates weighted similarity scores, and ranks songs to generate personalized recommendations. The project also explores how feature weighting and limited data can influence recommendation quality and introduce bias.

---

## How The System Works

### How Music Recommendation Systems Work

Major music streaming platforms predict what a user might enjoy by analyzing information about the user's listening behavior, the songs themselves, or a combination of both. These approaches are commonly called collaborative filtering and content-based filtering.

Collaborative filtering uses patterns in user behavior. For example, if two users often listen to and like similar songs, the system may recommend a song liked by one user to the other. Useful data can include likes, skips, listening history, repeated plays, and songs added to playlists.

Content-based filtering focuses on the attributes or features of songs. If a user frequently enjoys high-energy pop songs, the system can recommend other songs with similar characteristics. Song features might include genre, mood, tempo, and energy.

Many real-world recommendation systems combine these approaches. For this basic Python music recommender, content-based filtering is used because songs can be represented using features and compared directly with a user's preferences.

### My Recommendation System

This project simulates a simple content-based music recommendation system. It compares song attributes with a user's stated music preferences. Each song receives a weighted score based on how closely it matches the user's taste, and the highest-scoring songs are ranked as the top recommendations.

The song dataset includes the following features:

- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

For the initial scoring system, the recommender prioritizes:

- Genre
- Mood
- Energy

The `UserProfile` uses:

- Favorite genre
- Favorite mood
- Target energy

### Test User Profile

For the initial simulation, the recommender will use the following test profile:

```python
user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40
}
```

This profile helps test whether the recommender can distinguish between songs with very different characteristics, such as intense rock and chill lofi. Genre and mood provide categorical preferences, while target energy allows the system to measure how closely a song's energy level matches the user's preference.

### Recommendation Scoring Logic

The recommender uses a weighted scoring system to determine how closely each song matches the user's preferences. Genre receives the highest weight because it is treated as a strong indicator of musical preference. Mood provides an additional categorical match, while energy is scored according to its closeness to the user's target energy.

The finalized algorithm recipe is:

- **Genre match:** +2.0 points if the song's genre matches the user's favorite genre.
- **Mood match:** +1.0 point if the song's mood matches the user's favorite mood.
- **Energy similarity:** `1 - abs(song_energy - target_energy)`

For example, for a user who prefers `lofi`, `chill`, and a target energy of `0.40`, a lofi/chill song with an energy of `0.42` would receive:

```text
Genre match       = 2.00
Mood match        = 1.00
Energy similarity = 1 - abs(0.42 - 0.40)
                  = 0.98
----------------------------------------
Total score       = 3.98
```

The scoring rule is applied to every song in the catalog. After all songs receive a score, the ranking rule sorts them from highest to lowest. The highest-scoring songs become the personalized recommendations.

### Recommendation Flow

```text
INPUT
User Profile
- Favorite Genre: lofi
- Favorite Mood: chill
- Target Energy: 0.40
        |
        v
SONG CATALOG
Load songs from songs.csv
        |
        v
PROCESS
For Each Song:
- Check genre match (+2.0)
- Check mood match (+1.0)
- Calculate energy similarity
- Calculate total score
        |
        v
RANKING
Sort all songs by total score
from highest to lowest
        |
        v
OUTPUT
Return Top K
Personalized Recommendations
```

### Potential Biases

This simple recommender may over-prioritize genre because a genre match receives the highest fixed weight. As a result, songs from other genres that closely match the user's preferred mood or energy may rank lower.

The system may also create a filter bubble by repeatedly recommending music similar to the user's existing preferences, reducing opportunities to discover new genres or moods. Future versions could use more features, adjust feature weights, or introduce diversity into the final recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   **Mac or Linux:**

   ```bash
   source .venv/bin/activate
   ```

   **Windows PowerShell:**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Sample recommendation output will be added after the recommender is implemented.

---

## Experiments You Tried

Experiments with different feature weights and user profiles will be documented after implementation and testing.

---

## Limitations and Risks

The current design uses a small song catalog and a limited set of user preferences. The recommender may over-prioritize certain features, such as genre, and could repeatedly recommend similar music. Additional limitations will be evaluated after implementation and testing.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

A final reflection on recommendation predictions, bias, and fairness will be added after implementation and evaluation.