# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

## How The System Works

### How Music Recommendation Systems Work

Major music streaming platforms predict what a user might enjoy by analyzing information about the user's listening behavior, the songs themselves, or a combination of both. These approaches are commonly called collaborative filtering and content-based filtering.

Collaborative filtering uses patterns in user behavior. For example, if two users often listen to and like similar songs, the system may recommend a song liked by one user to the other. Useful data can include likes, skips, listening history, repeated plays, and songs added to playlists.

Content-based filtering focuses on the attributes or features of songs. If a user frequently enjoys high-energy pop songs, the system can recommend other songs with similar characteristics. Song features might include genre, mood, tempo, and energy.

Many real-world recommendation systems combine these approaches. For a basic Python music recommender, content-based filtering is a good starting point because each song can be represented using simple features such as genre, mood, tempo, and energy.

### My Recommendation System

This project simulates a simple content-based music recommendation system. This version focuses on comparing song attributes with a user's stated music preferences. Each song is scored based on how closely its features match the user's taste, and the songs with the highest scores are ranked as the top recommendations.

The `Song` object uses the following features:
- Genre
- Mood
- Energy
- Tempo

The `UserProfile` stores the user's preferences for:
- Preferred genre
- Preferred mood
- Preferred energy
- Preferred tempo

The recommender compares each song with the user's preferences using a weighted scoring rule. Genre and mood matches contribute to the score, while numerical features such as energy and tempo are scored based on how close they are to the user's preferred values. After every song receives a score, the recommender ranks the songs from highest to lowest score and returns the best matches.


### Recommendation Flow

```text
              USER DATA
          +----------------+
          |  UserProfile   |
          |----------------|
          | Preferred Genre|
          | Preferred Mood |
          | Preferred Energy|
          | Preferred Tempo|
          +--------+-------+
                   |
                   | Compare preferences
                   v
+------------------+------------------+
|                                     |
|             SONG CATALOG            |
|                                     |
|  Song 1       Song 2       Song 3   |
|  Genre        Genre        Genre    |
|  Mood         Mood         Mood     |
|  Energy       Energy       Energy   |
|  Tempo        Tempo        Tempo    |
|                                     |
+------------------+------------------+
                   |
                   | Weighted Scoring Rule
                   v
          +----------------+
          | Calculate Score|
          | for Each Song  |
          +--------+-------+
                   |
                   | Ranking Rule
                   v
          +----------------+
          | Rank Songs     |
          | Highest Score  |
          | to Lowest Score|
          +--------+-------+
                   |
                   v
          +----------------+
          | Personalized   |
          | Recommendations|
          +----------------+

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



