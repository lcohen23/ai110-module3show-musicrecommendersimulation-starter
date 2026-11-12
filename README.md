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

Real platforms like Spotify and YouTube blend two approaches: **collaborative filtering**, which recommends songs liked by users with similar behavior (plays, skips, likes, playlist adds), and **content-based filtering**, which recommends songs whose attributes (genre, tempo, energy, mood) resemble what you already like. My simulation is content-based, since it has a song catalog and a single user's taste profile but no other listeners. It will prioritize matching the user's preferred genre first, then how *close* a song's energy is to the user's target, with mood and acoustic sound as smaller factors.

**`Song` features:** `genre`, `mood`, `energy`, `acousticness` (plus `tempo_bpm`, `valence`, `danceability` stored for later experiments)

**`UserProfile` features:** `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

### Algorithm Recipe

Each song is scored out of 5.0:

- **+2.0** if the song's genre matches `favorite_genre`
- **+1.0** if the song's mood matches `favorite_mood`
- **up to +1.5** for energy closeness: `1.5 × (1 − |song.energy − target_energy|)`
- **up to +0.5** for acoustic fit: `0.5 × acousticness` if `likes_acoustic`, otherwise `0.5 × (1 − acousticness)`

Every song in the CSV is scored, the list is sorted from highest to lowest, and the top *k* are recommended.

### Expected Biases

- **Genre dominates.** A song in the wrong genre with the perfect mood and energy can still lose to a same-genre song with the wrong mood.
- **Exact matching is strict.** "indie pop" gets no credit from a "pop" fan, and "chill" gets none from a "relaxed" listener.
- **Small, uneven catalog.** Lofi has 3 songs, but most genres have only 1, so fans of rarer genres quickly run out of good matches.

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

Output of `python -m src.main` with the default pop/happy profile:

```
Loaded songs: 18

Profile: genre=pop, mood=happy, energy=0.8, likes_acoustic=False

Top recommendations:

1. Sunrise City by Neon Echo  [4.88 / 5.00]
     - genre match: pop (+2.0)
     - mood match: happy (+1.0)
     - energy 0.82 vs target 0.80 (+1.47)
     - acoustic fit (+0.41)

2. Gym Hero by Max Pulse  [3.78 / 5.00]
     - genre match: pop (+2.0)
     - energy 0.93 vs target 0.80 (+1.30)
     - acoustic fit (+0.47)

3. Rooftop Lights by Indigo Parade  [2.77 / 5.00]
     - mood match: happy (+1.0)
     - energy 0.76 vs target 0.80 (+1.44)
     - acoustic fit (+0.33)

4. Concrete Verses by Blockwise  [1.93 / 5.00]
     - energy 0.78 vs target 0.80 (+1.47)
     - acoustic fit (+0.46)

5. Night Drive Loop by Neon Echo  [1.81 / 5.00]
     - energy 0.75 vs target 0.80 (+1.42)
     - acoustic fit (+0.39)
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



