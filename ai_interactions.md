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