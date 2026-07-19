# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**TuneMatch 1.0**

---

## 2. Intended Use

TuneMatch 1.0 is designed to generate personalized music recommendations by matching song attributes to a user's musical preferences. It uses preferences such as genre, mood, target energy, detailed mood, popularity, release decade, instrumentalness, and speechiness to rank songs.

The recommender is designed for classroom exploration and learning about content-based recommendation systems. It is not intended for production use or for making recommendations to real users at scale because it uses a small fictional dataset and a simplified rule-based scoring system.

---

## 3. How the Model Works

TuneMatch 1.0 uses a content-based recommendation approach. The system takes two main types of input: song features from the dataset and a user's stated preferences. It then compares each song's attributes with the user's preferences and calculates a numeric score.

The original scoring logic used three main features: genre, mood, and energy. Genre and mood use exact-match scoring, while energy uses a similarity calculation based on how close the song's energy level is to the user's target energy.

The recommender was extended to include five additional song attributes:

- `popularity`
- `release_decade`
- `detailed_mood`
- `instrumentalness`
- `speechiness`

These advanced attributes also contribute to the recommendation score. Exact matches are used where appropriate, while numerical features use similarity calculations based on the distance between the song's value and the user's preference.

The recommender also supports three scoring modes using a simple Strategy-style design:

- `genre_first` — gives greater importance to matching the user's preferred genre.
- `mood_first` — gives greater importance to matching the user's preferred mood.
- `energy_focused` — gives greater importance to similarity between the song's energy and the user's target energy.

The user can switch between these scoring modes in `src/main.py`. The selected mode determines the weights used by the scoring function without requiring separate recommendation functions for each strategy.

After calculating the initial scores, the recommendation function ranks songs and applies diversity logic. A song can receive a penalty when its artist is already represented in the selected recommendations. A smaller genre penalty can also be applied when a genre is already heavily represented. This gives songs from different artists and genres a better opportunity to appear in the top results while still allowing highly relevant songs to remain competitive.

The final recommendations are presented in a formatted table containing Rank, Song, Artist, Score, and Reasons. The Reasons column explains the factors that contributed to each recommendation score, improving the transparency of the system.

---

## 4. Data

TuneMatch 1.0 uses a catalog of 20 fictional songs. The original dataset contained 10 songs, and 10 additional songs were added to increase the variety of genres and moods.

The catalog includes genres such as pop, lofi, rock, jazz, ambient, synthwave, indie pop, folk, reggae, drum and bass, world, hip hop, classical, and funk. It also includes moods such as happy, chill, intense, relaxed, focused, nostalgic, peaceful, romantic, adventurous, dreamy, confident, dramatic, and playful.

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

Five additional attributes were added as part of the advanced feature extension:

- `popularity`
- `release_decade`
- `detailed_mood`
- `instrumentalness`
- `speechiness`

The recommendation scoring logic uses genre, mood, energy, and the five advanced attributes. Other available attributes, such as tempo, valence, danceability, and acousticness, remain available for future extensions.

The dataset does not represent every type of musical taste and does not include real listening histories, lyrics, language preferences, likes, skips, or repeated-play behavior.

---

## 5. Strengths

TuneMatch 1.0 works well when a user's preferences have strong matches in the song catalog. The scoring system combines exact feature matches with numerical similarity calculations, allowing songs to receive credit for both categorical and continuous characteristics.

The multiple scoring modes also make the system more flexible. A user or developer can change whether genre, mood, or energy has greater influence over the ranking without rewriting the entire recommendation algorithm.

The recommendations matched my expectations for several test profiles. For the Chill Lofi profile, `Library Rain` ranked highly because it matched the lofi genre and chill mood and had an energy level close to the user's target. For the Intense Rock profile, `Storm Runner` ranked highly because it matched the rock genre, intense mood, and high target energy.

The advanced attributes provide additional information for distinguishing songs that may otherwise have similar baseline scores. The diversity penalty also helps reduce repeated artists and excessive genre concentration in the top recommendations.

Finally, the formatted summary table and score explanations make the recommendation process easier to understand by showing both the ranking and the reasons behind each recommendation.

---

## 6. Limitations and Bias

TuneMatch 1.0 uses a small catalog of only 20 fictional songs. Some genres and moods have more representation than others, which means users whose preferences align with better-represented categories may receive stronger recommendations.

The recommendation results are also influenced by manually selected scoring weights. For example, the `genre_first` mode gives greater importance to genre, while the `mood_first` and `energy_focused` modes prioritize different characteristics. These design choices can affect which songs appear at the top of the ranking.

The five advanced attributes improve the scoring system but are also based on manually assigned values in a fictional dataset. They do not represent measurements or behavioral data from a real music platform.

The diversity logic helps reduce repetition by penalizing songs when the same artist is already represented and by applying a smaller penalty when a genre is already heavily represented. This can improve fairness in the recommendation list by giving other artists and genres a better opportunity to appear and by reducing the risk of repeatedly recommending very similar content.

However, the diversity penalty does not completely eliminate bias or filter bubbles. Songs must still receive sufficiently high relevance scores to appear in the top results, and the small dataset limits how much variety the system can provide. The fixed diversity penalties may also not reflect every user's preferences; some users may prefer multiple songs from the same artist or genre.

---

## 7. Evaluation

I evaluated the recommender using four different user profiles: High-Energy Pop, Chill Lofi, Intense Rock, and a Conflicting Preferences edge case combining pop, chill, and high energy.

For each profile, I examined the top five recommendations to determine whether the highest-ranked songs reasonably matched the requested genre, mood, and target energy. I also compared the profiles and ran a weight-shift experiment to test how sensitive the recommendations were to changes in the scoring logic.

**The profile outputs below document the baseline scoring experiment completed before the advanced stretch features were added. The final implementation extends this baseline with advanced attributes, multiple scoring modes, diversity penalties, and formatted table output.**

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

The recommendations generally matched my expectations when the user's preferences were consistent. For example, `Library Rain` ranked first for the Chill Lofi profile because it matched both the lofi genre and chill mood, while its energy of 0.35 was close to the target of 0.30.

Similarly, `Storm Runner` ranked first for the Intense Rock profile because it matched the rock genre and intense mood and had an energy level close to the target.

The most surprising result came from the Conflicting Preferences profile. `Gym Hero` ranked first even though it did not match the requested chill mood. Its pop genre match and energy similarity gave it a strong score. This demonstrated how feature weights can determine which preferences dominate when a user's preferences conflict.

### Profile Comparisons

**High-Energy Pop vs. Chill Lofi:** The High-Energy Pop profile favored `Sunrise City` and `Gym Hero`, while the Chill Lofi profile favored `Library Rain` and `Midnight Coding`. This difference makes sense because the first profile emphasizes pop and high energy, while the second emphasizes lofi, chill music, and lower energy.

**Intense Rock vs. Conflicting Preferences:** The Intense Rock profile ranked `Storm Runner` first because it matched the rock genre, intense mood, and high target energy. The Conflicting Preferences profile ranked `Gym Hero` first because its pop genre and high energy matched two important parts of the profile despite not matching the chill mood.

These comparisons demonstrate how different user preferences and scoring weights influence the final rankings.

### Weight-Shift Experiment

I tested how sensitive the recommender was to changes in the scoring weights. In the original scoring logic, a genre match received +2.0 points, a mood match received +1.0 point, and energy similarity was calculated as:

`1 - abs(song_energy - target_energy)`

For the experiment, I reduced the genre weight from +2.0 to +1.0 and doubled the maximum contribution of energy similarity from 1.0 to 2.0. The mood weight remained unchanged at +1.0.

The experiment did not change the top-ranked song for any of the four profiles, but some lower rankings changed. For the Chill Lofi profile, `Spacewalk Thoughts` moved above `Focus Flow` because its energy was closer to the user's target. For the Conflicting Preferences profile, high-energy songs such as `Storm Runner` and `Midnight Cipher` entered the top five while some chill songs dropped out.

Overall, the weight shift made the recommendations more sensitive to energy rather than clearly more accurate. This experiment demonstrated that changing feature weights can significantly affect which characteristics dominate the recommendations.

### Diversity Evaluation

I also evaluated the diversity penalty after implementing the advanced recommendation logic. The recommender checks artists and genres that are already represented while building the top recommendations.

For the Chill Lofi profile, `Focus Flow` received a repeat artist diversity penalty of `-1.0` and a repeat genre diversity penalty of `-0.5`. The song was still able to remain in the recommendation list because its relevance score was sufficiently high.

This test demonstrated that the diversity component does not automatically remove repeated artists or genres. Instead, it reduces their scores and gives other relevant songs a better opportunity to appear in the top results.

---

## 8. Future Work

Future versions of TuneMatch 1.0 could incorporate additional existing features such as tempo, valence, danceability, and acousticness directly into the recommendation scoring system.

The scoring weights and diversity penalties could also become configurable so users can control how much importance they place on genre, mood, energy, novelty, and artist variety.

A larger and more balanced dataset would improve coverage across different genres, moods, artists, and musical styles. Using real music metadata could also make the evaluation more realistic.

A more advanced version could learn from user behavior such as likes, skips, repeated plays, ratings, and listening history. This would allow the system to combine content-based recommendation with collaborative filtering or other machine learning approaches.

The diversity component could also be extended beyond fixed artist and genre penalties by measuring similarity between recommended songs or automatically balancing relevance and novelty based on individual user preferences.

---

## 9. Personal Reflection

This project helped me understand how recommender systems turn user preferences and item features into ranked suggestions. My biggest learning moment was seeing how much feature selection and scoring weights affect the final recommendations.

I was surprised that a relatively simple content-based scoring algorithm could still produce recommendations that seemed reasonable when songs closely matched a user's preferences. Adding advanced attributes also showed me how additional features can make scoring more detailed, while experimenting with multiple ranking modes demonstrated that there is no single weighting strategy that works best for every type of user.

The diversity extension helped me understand another challenge in recommendation systems. Ranking only by relevance can repeatedly recommend similar artists or genres, while adding diversity logic can provide users with more varied results. At the same time, too much diversity could reduce relevance, so recommendation systems need to balance both goals.

The visual summary table also improved my understanding of explainable recommendations. Showing the score and reasons for each recommendation makes it easier to understand why the system ranked one song above another.

AI tools helped me brainstorm advanced song features, explore a Strategy-style design for multiple scoring modes, implement and document the diversity logic, and improve the presentation of the recommendation results. However, I still needed to review the suggestions, run the code, inspect the outputs, compare rankings, and verify that each change behaved as expected.

This project changed how I think about real music recommendation applications. Even simple recommendation rules can feel personalized, but the results depend heavily on the available data, selected features, scoring weights, ranking strategy, and diversity rules. If I extended this project further, I would use a larger real-world dataset, incorporate user behavior, and explore ways to automatically balance relevance, diversity, and novelty.