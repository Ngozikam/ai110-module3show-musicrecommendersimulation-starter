# 🎵 Music Recommender Simulation

## Project Summary

This project builds a content-based music recommender in Python. It compares song features with a user's taste profile, calculates weighted similarity scores, and ranks songs to generate personalized recommendations.

The project begins with a simple scoring system based on genre, mood, and energy and extends it with advanced song attributes, multiple ranking strategies, diversity logic, and explainable recommendation output.

The project also explores how feature weighting, dataset limitations, and ranking decisions can influence recommendation quality, diversity, and bias.

---

## How the System Works

### How Music Recommendation Systems Work

Major music streaming platforms predict what a user might enjoy by analyzing information about the user's listening behavior, the songs themselves, or a combination of both. Two common approaches are collaborative filtering and content-based filtering.

**Collaborative filtering** uses patterns in user behavior. For example, if two users often listen to and like similar songs, the system may recommend a song liked by one user to the other. Useful behavioral data can include likes, skips, listening history, repeated plays, ratings, and songs added to playlists.

**Content-based filtering** focuses on the attributes or features of songs. If a user frequently enjoys high-energy pop songs, the system can recommend other songs with similar characteristics. Song features might include genre, mood, tempo, energy, valence, danceability, and acousticness.

Many real-world recommendation systems combine collaborative and content-based approaches. This Python project focuses on content-based filtering because songs can be represented using structured features and compared directly with a user's stated preferences.

---

## My Recommendation System

This project simulates a content-based music recommendation system. It takes two main types of input:

1. **Song data** — attributes describing each song.
2. **User preferences** — attributes describing the type of music the user prefers.

The recommender compares each song with the user's preferences, calculates a numeric score, and ranks the songs from highest to lowest. The highest-scoring songs become the top recommendations.

The final system also applies diversity logic during ranking to reduce excessive repetition of the same artists and genres.

---

## Song Dataset

The recommender loads a structured dataset containing **20 fictional songs** from `data/songs.csv`.

The baseline song attributes are:

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

As an advanced extension, five additional attributes were added:

- `popularity`
- `release_decade`
- `detailed_mood`
- `instrumentalness`
- `speechiness`

The recommendation scoring logic uses genre, mood, energy, and the five advanced attributes. Other available attributes such as tempo, valence, danceability, and acousticness remain available for future extensions.

---

## User Preferences

The final recommender supports user preferences including:

- Preferred genre
- Preferred mood
- Target energy
- Detailed mood
- Popularity preference
- Release decade
- Instrumentalness
- Speechiness

The application evaluates multiple user profiles, including:

- High-Energy Pop
- Chill Lofi
- Intense Rock
- Conflicting Preferences

Using multiple profiles makes it possible to observe how different preferences affect the ranking results.

---

## Baseline Recommendation Scoring Logic

The initial version of the recommender used three main features:

- Genre
- Mood
- Energy

The baseline scoring recipe was:

- **Genre match:** +2.0 points if the song's genre matches the user's preferred genre.
- **Mood match:** +1.0 point if the song's mood matches the user's preferred mood.
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

This baseline scoring system was later extended with advanced song attributes and configurable scoring modes.

---

## Advanced Recommendation Features

### Advanced Song Attributes

The final scoring system incorporates five additional song attributes:

- Popularity
- Release decade
- Detailed mood
- Instrumentalness
- Speechiness

These features provide additional information for distinguishing between songs that may have similar genre, mood, or energy values.

Categorical features use matching logic where appropriate, while numerical features use similarity calculations.

---

## Multiple Scoring Modes

The recommender supports three different ranking strategies:

- `genre_first` — gives greater importance to matching the user's preferred genre.
- `mood_first` — gives greater importance to matching the user's preferred mood.
- `energy_focused` — gives greater importance to similarity between the song's energy and the user's target energy.

The scoring mode can be selected in `src/main.py`.

A simple Strategy-style design is used so the scoring behavior can change without creating separate recommendation functions for every ranking strategy.

The default scoring mode is:

```python
scoring_mode = "genre_first"
```

It can be changed to:

```python
scoring_mode = "mood_first"
```

or:

```python
scoring_mode = "energy_focused"
```

This makes it possible to experiment with how different feature priorities affect recommendation rankings.

---

## Diversity and Fairness Logic

Ranking songs only by relevance can result in repeated recommendations from the same artist or genre. To reduce this problem, the recommender applies a diversity penalty while selecting the top recommendations.

If an artist is already represented in the selected recommendations, another song from the same artist can receive a score penalty.

The recommender can also apply a smaller penalty when a genre is already heavily represented.

For example, during testing with the Chill Lofi profile, `Focus Flow` received:

- Repeat artist diversity penalty: `-1.0`
- Repeat genre diversity penalty: `-0.5`

The diversity logic does not automatically remove repeated artists or genres. Instead, it lowers their adjusted scores and gives other relevant songs a better opportunity to appear.

This helps reduce excessive repetition and can improve the variety and fairness of the recommendation list while still allowing highly relevant songs to remain competitive.

---

## Recommendation Flow

```text
INPUT
User Preferences
        |
        v
SONG CATALOG
Load 20 songs from data/songs.csv
        |
        v
SCORING MODE
Select:
- Genre-First
- Mood-First
- Energy-Focused
        |
        v
SCORING
For Each Song:
- Evaluate genre match
- Evaluate mood match
- Calculate energy similarity
- Evaluate detailed mood
- Calculate popularity similarity
- Evaluate release decade
- Calculate instrumentalness similarity
- Calculate speechiness similarity
        |
        v
INITIAL RANKING
Sort songs by relevance score
        |
        v
DIVERSITY LOGIC
Apply artist and genre penalties
when appropriate
        |
        v
FINAL RANKING
Select Top K recommendations
        |
        v
OUTPUT
Display formatted table with:
- Rank
- Song
- Artist
- Score
- Reasons
```

---

## Explainable Recommendations

Each recommendation includes an explanation showing why the song received its score.

The explanation can include contributions such as:

```text
genre match (+3.0)
mood match (+1.0)
energy similarity (+0.92)
detailed mood match (+0.5)
popularity similarity (+0.49)
release decade match (+0.5)
instrumentalness similarity (+0.50)
speechiness similarity (+0.50)
```

When applicable, the explanation can also show diversity penalties such as:

```text
repeat artist diversity penalty (-1.0)
repeat genre diversity penalty (-0.5)
```

These explanations make the recommendation process more transparent and help users understand why one song ranks above another.

---

## Visual Summary Table

The final application uses the `tabulate` library to display recommendations in a formatted table.

Each user profile receives a table containing:

- Rank
- Song
- Artist
- Score
- Reasons

Example:

| Rank | Song | Artist | Score | Reasons |
|:---:|---|---|---:|---|
| 1 | Sunrise City | Neon Echo | 7.41 | Genre match, mood match, energy similarity, and advanced feature similarities |
| 2 | Gym Hero | Max Pulse | 5.94 | Genre match, strong energy similarity, and advanced feature similarities |
| 3 | Rooftop Lights | Indigo Parade | 3.30 | Mood match, energy similarity, and advanced feature similarities |

The actual terminal output displays the complete scoring explanation in the Reasons column.

---

## Getting Started

### Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment.

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

4. Run the recommender:

   ```bash
   python -m src.main
   ```

---

## Running Tests

Run the automated tests from the project root using:

```bash
python -m pytest -v
```

The current test suite verifies that:

- Recommendations are returned in score order.
- Recommendation explanations return non-empty text.

At final verification, the test suite completed successfully with:

```text
2 passed
```

---

## Experiments

The recommender was evaluated using four different user profiles:

- High-Energy Pop
- Chill Lofi
- Intense Rock
- Conflicting Preferences

The results showed that different preferences produced different recommendation rankings.

For example, the Chill Lofi profile favored songs such as `Library Rain` and `Midnight Coding`, while the Intense Rock profile strongly favored `Storm Runner`.

A weight-shift experiment was also performed to examine how changing the importance of genre and energy affected the rankings. The experiment showed that increasing the importance of energy caused songs with closer energy values to move higher in some recommendation lists.

The three scoring modes were also tested to observe how emphasizing genre, mood, or energy changes the ranking behavior.

Detailed experimental results and profile outputs are documented in [`model_card.md`](model_card.md).

---

## Limitations and Risks

The recommender uses a small dataset containing only 20 fictional songs. This limits the number of possible recommendations and does not represent the diversity of a real music catalog.

Some genres and moods are better represented than others, which can influence recommendation quality.

The scoring weights are manually selected. Different weights can produce different rankings and may over-prioritize certain features.

The advanced song attributes also use manually assigned values rather than measurements from a real music platform.

The diversity penalty helps reduce repeated artists and excessive genre concentration, but it does not completely eliminate filter bubbles or recommendation bias.

The system also does not use real user behavior such as:

- Listening history
- Likes
- Skips
- Repeated plays
- Ratings
- Playlist additions

A production recommendation system would require a much larger dataset, real user behavior, more extensive evaluation, and more sophisticated recommendation algorithms.

---

## Potential Improvements

Future versions could:

- Incorporate tempo, valence, danceability, and acousticness directly into scoring.
- Use a larger and more balanced real-world music dataset.
- Learn user preferences from listening behavior.
- Combine content-based filtering with collaborative filtering.
- Make scoring weights configurable by the user.
- Make diversity penalties configurable.
- Measure similarity between recommended songs.
- Automatically balance relevance, diversity, and novelty.
- Add additional automated tests for advanced scoring modes and diversity behavior.

---

## Project Reflection

This project demonstrated how a recommendation system converts item features and user preferences into ranked suggestions.

The experiments showed that feature selection and scoring weights strongly influence recommendation results. The multiple scoring modes demonstrated that different ranking strategies can prioritize different aspects of a user's preferences.

The diversity extension also demonstrated the trade-off between relevance and variety. Recommending only the highest-scoring songs can produce repetitive results, while diversity penalties can give other artists and genres a better opportunity to appear.

Finally, displaying recommendation scores and reasons in a formatted table improved transparency by making it easier to understand why each song was recommended.

For a detailed discussion of the dataset, algorithm, experiments, limitations, bias, fairness, and personal reflection, see the:

[**Model Card**](model_card.md)

For documentation of how AI tools contributed to the stretch features, see:

[**AI Interactions Log**](ai_interactions.md)