# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI coding assistant to help extend the music recommender by adding at least five advanced song attributes that were not included in the baseline dataset. The goal was to add more detailed song information that could later be incorporated into the recommendation scoring logic.

**Prompts used:**

"Suggest five or more advanced song attributes that are not currently included in my dataset. My existing attributes are id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. The new features should include a mix of numerical and categorical attributes that can be used to improve a content-based music recommender."

"Update my 20-song CSV dataset by adding the selected advanced attributes while preserving all existing song data. Use realistic values for each new attribute."

**What did the agent generate or change?**

The AI suggested five additional attributes: `popularity`, `release_decade`, `detailed_mood`, `instrumentalness`, and `speechiness`. It generated values for these attributes for all 20 songs in `data/songs.csv` while preserving the existing song information.

**What did you verify or fix manually?**

I reviewed the updated CSV structure to confirm that all 20 songs contained values for the five new attributes and that the original song data was preserved. I checked that popularity values were between 0 and 100 and that instrumentalness and speechiness values were between 0.0 and 1.0. I updated the CSV loader to convert the new numerical attributes to the correct Python data types and verified that the recommender ran successfully with all four test profiles. I also confirmed that the advanced attributes contributed to the recommendation scores and appeared correctly in the explanations.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

I used a simple Strategy-style pattern to support multiple recommendation scoring modes: `genre_first`, `mood_first`, and `energy_focused`.

**How did AI help you brainstorm or implement it?**

I asked the AI coding assistant to suggest a modular way to support multiple ranking strategies without duplicating the recommendation logic. The AI suggested a Strategy-style approach where each scoring mode uses different weights for genre, mood, and energy. I reviewed the suggestion and implemented a simple dictionary of strategy weights that fits the scope of this project.

**How does the pattern appear in your final code?**

The pattern appears in the `score_song()` function in `src/recommender.py`, where the selected `mode` determines which set of scoring weights is used. The `recommend_songs()` function passes the selected mode to `score_song()`, and `src/main.py` allows the scoring mode to be changed between `genre_first`, `mood_first`, and `energy_focused`.

---

## Diversity and Fairness Logic

**Prompt used:**

"Update my music recommender to add a diversity penalty during ranking. If a song's artist is already represented in the current top recommendations, reduce that song's score so songs from different artists have a better chance of appearing. Also consider preventing too many songs from the same genre. Keep the existing scoring modes and advanced song features unchanged, and implement the diversity logic in a simple, readable way without modifying the original `score_song()` calculation."

**What was implemented:**

The recommendation logic now applies a diversity penalty when an artist is already represented in the selected recommendations. It also applies a smaller penalty when a genre is already heavily represented. Penalized songs can still be recommended if their adjusted scores remain high enough.

**Manual verification:**

I tested the recommender with the existing user profiles. For the Chill Lofi profile, `Focus Flow` received both a repeat artist penalty of `-1.0` and a repeat genre penalty of `-0.5`. This confirmed that the diversity logic was applied while still allowing highly relevant songs to remain in the recommendations.

---

## Visual Summary Table

**Prompt used:**

"Update the terminal output of my Python music recommender to display the top recommendations in a formatted table using the `tabulate` library. The table should include Rank, Song, Artist, Score, and Reasons for each recommendation. Keep the existing advanced features, multiple scoring modes, and diversity penalty unchanged. The Reasons column must show the explanation for each song's score. Keep the implementation simple and readable."

**What was implemented:**

The terminal output was updated using the `tabulate` library. Each user profile now displays its top five recommendations in a formatted table with Rank, Song, Artist, Score, and Reasons columns.

**Sample output — High-Energy Pop:**

| Rank | Song | Artist | Score | Reasons |
|:---:|---|---|---:|---|
| 1 | Sunrise City | Neon Echo | 7.41 | Strong genre, mood, and energy match |
| 2 | Gym Hero | Max Pulse | 5.94 | Strong genre and energy match |
| 3 | Rooftop Lights | Indigo Parade | 3.30 | Mood and energy match |
| 4 | Concrete Pulse | Eastline Crew | 2.77 | Strong energy similarity |
| 5 | Midnight Cipher | Vector Bloom | 2.61 | Strong energy similarity |

The table above summarizes the main reasons for each recommendation. The detailed scoring contributions for the top recommendation are shown below.

**Detailed reasoning for `Sunrise City`:**

- Genre match: `+3.0`
- Mood match: `+1.0`
- Energy similarity: `+0.92`
- Detailed mood match: `+0.5`
- Popularity similarity: `+0.49`
- Release decade match: `+0.5`
- Instrumentalness similarity: `+0.50`
- Speechiness similarity: `+0.50`

**Total score: `7.41`**

**Diversity penalty example:**

For the Chill Lofi profile, `Focus Flow` received:

- Repeat artist diversity penalty: `-1.0`
- Repeat genre diversity penalty: `-0.5`

This demonstrates that the recommender keeps the table readable while still providing detailed score explanations and showing how the diversity logic affects ranking.

**Manual verification:**

I ran the recommender and verified that each of the four user profiles displays a separate formatted table. I also confirmed that each table contains the required Rank, Song, Artist, Score, and Reasons columns. The existing scoring modes, advanced song features, and diversity penalties continued to work after the output formatting was changed.