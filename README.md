# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version is called **VibeCheck 1.0**. It recommends the top 5 songs from an 18-song catalog. The user picks a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music. Each song gets a score based on how well it matches. Every recommendation shows the reasons behind its score.

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

The default High-Energy Pop profile (first of the 6 profiles `python -m src.main` prints):

```
=== High-Energy Pop ===
Profile: genre=pop, mood=happy, energy=0.8, likes_acoustic=False

1. Sunrise City by Neon Echo  [4.88]
     - genre match: pop (+2.0)
     - mood match: happy (+1.0)
     - energy 0.82 vs target 0.80 (+1.47)
     - acoustic fit (+0.41)
2. Gym Hero by Max Pulse  [3.78]
     - genre match: pop (+2.0)
     - energy 0.93 vs target 0.80 (+1.30)
     - acoustic fit (+0.47)
3. Rooftop Lights by Indigo Parade  [2.77]
     - mood match: happy (+1.0)
     - energy 0.76 vs target 0.80 (+1.44)
     - acoustic fit (+0.33)
4. Concrete Verses by Blockwise  [1.93]
     - energy 0.78 vs target 0.80 (+1.47)
     - acoustic fit (+0.46)
5. Night Drive Loop by Neon Echo  [1.81]
     - energy 0.75 vs target 0.80 (+1.42)
     - acoustic fit (+0.39)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- **Six user profiles.** I tested three normal listeners (pop, lofi, rock) and three tricky ones. The tricky ones were a "sad but high-energy" user, a genre not in the catalog (k-pop), and the pop profile typed with capital letters. Full outputs are in the [model card](model_card.md).
- **Weight shift.** I cut the genre weight from 2.0 to 1.0 and doubled energy from 1.5 to 3.0. Rooftop Lights passed Gym Hero for the pop fan, which felt better. But the k-pop fan got a country song at #2, which felt worse. The results were different, not clearly better, so I kept the original weights.

---

## Limitations and Risks

- **Exact word matching.** "indie pop" gets no credit from a pop fan. Typing "Pop" instead of "pop" gets no genre or mood points at all.
- **Labels beat sound.** A user who wanted high energy got a quiet folk song at #1 because its genre and mood matched.
- **Tiny, uneven catalog.** Only 18 songs. Lofi has 3, but most genres have just 1.
- **No real listening data.** It ignores lyrics, popularity, and what people actually play or skip.

More detail is in the model card.

---

## Reflection

Full details are in the [**Model Card**](model_card.md).

A recommender doesn't need to be complicated to feel smart. Mine is just a checklist: points for matching genre and mood, and points for being close in energy. Then it sorts the songs. Even so, a pop fan getting Sunrise City at #1 feels like a real recommendation. Real apps also score and rank songs, but they use far more data and signals, like skips, replays, and what similar users liked.

Bias can come from small choices. Giving genre the most points meant one label could beat everything else. Lofi fans got three strong matches, but metal and folk fans got only one, just because of what was in the catalog. Exact word matching meant a capital letter could ruin a whole list. None of this was on purpose, but it would still treat some users worse than others.
