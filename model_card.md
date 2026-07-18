# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TuneMatch 1.0**

---

## 2. Intended Use  

TuneMatch 1.0 is designed to generate personalized music recommendations by matching songs to a user's preferred genre, mood, and energy level. It assumes that these stated preferences provide a useful representation of the user's current musical taste.

The recommender is designed for classroom exploration and learning about content-based recommendation systems. It is not intended for production use or for making recommendations to real users at scale because it uses a small dataset and a simplified scoring system.

---

## 3. How the Model Works  


TuneMatch 1.0 uses a simple content-based scoring approach. It compares each song's genre, mood, and energy with the user's preferred genre, mood, and target energy.

A song receives 2 points when its genre matches the user's preferred genre and 1 point when its mood matches the user's preferred mood. Energy is scored based on how close the song's energy level is to the user's target energy. Songs with closer energy values receive higher similarity scores.

The model calculates a total score for every song, ranks the songs from highest to lowest score, and returns the top recommendations with reasons explaining each score. The starter logic was expanded to load song data from a CSV file, calculate weighted preference scores, rank the songs, and provide explanations for the recommendations.

---

## 4. Data  


TuneMatch 1.0 uses a catalog of 20 fictional songs. The original dataset contained 10 songs, and 10 additional songs were added to increase the variety of genres and moods.

The catalog includes genres such as pop, lofi, rock, jazz, ambient, synthwave, indie pop, folk, reggae, drum and bass, world, hip hop, classical, and funk. It also includes a range of moods such as happy, chill, intense, relaxed, focused, nostalgic, peaceful, romantic, adventurous, dreamy, confident, dramatic, and playful.

Each song contains features including genre, mood, energy, tempo, valence, danceability, and acousticness. However, the current scoring system uses only genre, mood, and energy. The dataset does not represent every type of musical taste and does not include features such as lyrics, language, listening history, or user behavior.

---  


## 5. Strengths  


TuneMatch 1.0 works well when a user's genre, mood, and energy preferences are consistent. The scoring system correctly gives higher rankings to songs that match multiple preferences while also considering how close the song's energy is to the user's target.

The recommendations matched my expectations for several test profiles. For the Chill Lofi profile, `Library Rain` ranked first because it matched both the lofi genre and chill mood and had an energy level close to the user's target. For the Intense Rock profile, `Storm Runner` ranked first because it matched the rock genre, intense mood, and high target energy. These results show that the scoring system can produce reasonable recommendations when the song catalog contains strong matches for the user's preferences.

---

## 6. Limitations and Bias

The recommender considers only genre, mood, and energy in its current scoring logic, so it does not account for other aspects of musical taste such as tempo, valence, danceability, acousticness, lyrics, language, or listening history. The small 20-song catalog also means that some genres and moods have limited representation, which may produce weaker recommendations for users whose preferences are not well represented.

The original scoring system gives genre the highest fixed weight, so it may over-prioritize genre and rank a genre-matching song highly even when it does not match the user's preferred mood. The weight-shift experiment also showed that increasing the importance of energy can cause energy similarity to dominate other preferences. These limitations may favor users whose tastes align with strongly weighted or better-represented features and may contribute to a filter-bubble effect that reduces exposure to diverse music.

---

## 7. Evaluation

I evaluated the recommender using four different user profiles: High-Energy Pop, Chill Lofi, Intense Rock, and a Conflicting Preferences edge case combining pop, chill, and high energy. For each profile, I examined the top five recommendations to determine whether the highest-ranked songs reasonably matched the requested genre, mood, and target energy. I also compared the profiles and ran a weight-shift experiment to test how sensitive the recommendations were to changes in the scoring logic.

### High-Energy Pop

```text
Preferences: genre=pop, mood=happy, energy=0.9

Top recommendations:

Sunrise City - Score: 3.92
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.92)

Gym Hero - Score: 2.97
Because: genre match (+2.0), energy similarity (+0.97)

Rooftop Lights - Score: 1.86
Because: mood match (+1.0), energy similarity (+0.86)

Storm Runner - Score: 0.99
Because: energy similarity (+0.99)

Midnight Cipher - Score: 0.95
Because: energy similarity (+0.95)
```

### Chill Lofi

```text
Preferences: genre=lofi, mood=chill, energy=0.3

Top recommendations:

Library Rain - Score: 3.95
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.95)

Midnight Coding - Score: 3.88
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.88)

Focus Flow - Score: 2.90
Because: genre match (+2.0), energy similarity (+0.90)

Spacewalk Thoughts - Score: 1.98
Because: mood match (+1.0), energy similarity (+0.98)

Quiet Pines - Score: 0.98
Because: energy similarity (+0.98)
```

### Intense Rock

```text
Preferences: genre=rock, mood=intense, energy=0.9

Top recommendations:

Storm Runner - Score: 3.99
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.99)

Gym Hero - Score: 1.97
Because: mood match (+1.0), energy similarity (+0.97)

Midnight Cipher - Score: 1.95
Because: mood match (+1.0), energy similarity (+0.95)

Concrete Pulse - Score: 0.93
Because: energy similarity (+0.93)

Sunrise City - Score: 0.92
Because: energy similarity (+0.92)
```

### Conflicting Preferences (Edge Case)

```text
Preferences: genre=pop, mood=chill, energy=0.9

Top recommendations:

Gym Hero - Score: 2.97
Because: genre match (+2.0), energy similarity (+0.97)

Sunrise City - Score: 2.92
Because: genre match (+2.0), energy similarity (+0.92)

Midnight Coding - Score: 1.52
Because: mood match (+1.0), energy similarity (+0.52)

Library Rain - Score: 1.45
Because: mood match (+1.0), energy similarity (+0.45)

Spacewalk Thoughts - Score: 1.38
Because: mood match (+1.0), energy similarity (+0.38)
```

### Accuracy and Surprises

The recommendations generally matched my expectations when the user's preferences were consistent. For example, `Library Rain` ranked first for the Chill Lofi profile because it matched both the lofi genre and chill mood, while its energy of 0.35 was close to the target of 0.30. Similarly, `Storm Runner` ranked first for the Intense Rock profile because it matched the rock genre and intense mood and had an energy level close to the target.

The most surprising result came from the Conflicting Preferences profile. `Gym Hero` ranked first even though it did not match the requested chill mood. Its pop genre match contributed +2.0 points, and its energy closely matched the target of 0.9. This showed that the original scoring system can prioritize genre over mood when user preferences conflict.

### Profile Comparisons

**High-Energy Pop vs. Chill Lofi:** The High-Energy Pop profile favored `Sunrise City` and `Gym Hero`, while the Chill Lofi profile favored `Library Rain` and `Midnight Coding`. This difference makes sense because the first profile emphasizes pop and high energy, while the second emphasizes lofi, chill music, and lower energy.

**Intense Rock vs. Conflicting Preferences:** The Intense Rock profile ranked `Storm Runner` first because it matched the rock genre, intense mood, and high target energy. The Conflicting Preferences profile ranked `Gym Hero` first because its pop genre and high energy matched two important parts of the profile, despite not matching the chill mood. This comparison shows how the scoring weights influence which preference becomes most important when preferences conflict.

### Weight Shift Experiment

To test the system's sensitivity, I reduced the genre match weight from +2.0 to +1.0 and doubled the maximum contribution of energy similarity from 1.0 to 2.0. The mood weight remained unchanged at +1.0.

The experiment did not change the top-ranked song for any of the four profiles, but some lower rankings changed. For the Chill Lofi profile, `Spacewalk Thoughts` moved above `Focus Flow` because its energy was closer to the user's target. For the Conflicting Preferences profile, high-energy songs such as `Storm Runner` and `Midnight Cipher` entered the top five, while some chill songs dropped out.

Overall, the weight shift made the recommendations more sensitive to energy rather than clearly more accurate. This experiment showed that changing feature weights can significantly affect which characteristics dominate the recommendations.


### Weight-Shift Experiment

I tested how sensitive the recommender was to changes in the scoring weights. In the original scoring logic, a genre match received +2.0 points, a mood match received +1.0 point, and energy similarity was calculated as:

`1 - abs(song_energy - target_energy)`

For the experiment, I reduced the genre weight from +2.0 to +1.0 and doubled the energy similarity score. The mood weight remained unchanged at +1.0.

The experiment changed some of the rankings because songs with energy levels close to the user's target became more competitive, even when they did not match the preferred genre. For example, in the Chill Lofi profile, Spacewalk Thoughts moved above Focus Flow because its energy was closer to the user's target, even though Focus Flow matched the preferred lofi genre. This showed that changing feature weights can significantly affect which songs appear in the top recommendations. The experimental weights made the recommendations different rather than clearly more accurate.

---

## 8. Future Work  


Future versions of TuneMatch 1.0 could use more song features, such as tempo, valence, danceability, and acousticness, when calculating recommendations. The system could also provide clearer explanations showing how each preference contributed to a song's final ranking.

To improve diversity, the recommender could include some songs outside the user's usual genre or mood instead of always favoring the closest matches. A more advanced version could also learn from user behavior, such as likes, skips, repeated plays, and listening history, to handle more complex and changing musical tastes.

---


## 9. Personal Reflection  

This project helped me understand how recommender systems turn user preferences and item features into ranked suggestions. My biggest learning moment was seeing how much the feature weights affect the final recommendations. I was surprised that a simple scoring algorithm could still produce recommendations that seemed reasonable when a song closely matched a user's genre, mood, and energy preferences.

AI tools helped me brainstorm the scoring logic, implement functions, analyze results, and identify possible biases. However, I still needed to review the suggestions, run the code, compare the outputs, and verify that changes to the scoring weights produced reasonable results. This showed me that AI can support the engineering process, but the developer still needs to understand and validate the system's behavior.

The project also changed how I think about real music recommendation apps. Even simple recommendation rules can feel personalized, but the results depend heavily on the data, features, and weights chosen by the system designer. If I extended this project, I would add more song features, incorporate user behavior such as likes and skips, and explore ways to provide more diverse recommendations.

---