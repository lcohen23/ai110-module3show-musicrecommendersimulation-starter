# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeCheck 1.0**

---

## 2. Intended Use  

**Goal:** VibeCheck picks 5 songs for one listener from a catalog of 18. The user gives four settings: a favorite genre, a favorite mood, a target energy (0 to 1), and whether they like acoustic music. Each pick comes with its reasons.

It assumes four settings can describe a person's taste. It also assumes the user spells genre and mood words exactly like the catalog does.

**Intended use:** Classroom exploration. It shows how a content-based recommender turns data into suggestions, and where it goes wrong.

**Not intended for:** A real music app or real users. It doesn't learn from what people play. It only knows 18 songs. It breaks on capital letters. A low score doesn't mean a song is bad. It just means the song doesn't fit that one profile.

---

## 3. How the Model Works  

VibeCheck gives every song a score out of 5, like a checklist:

- **2 points** if the song's genre matches the user's favorite genre.
- **1 point** if the song's mood matches the user's favorite mood.
- **Up to 1.5 points for energy.** A song right at the user's target gets all 1.5. The further away it is, the fewer points it gets. Louder is not automatically better.
- **Up to 0.5 points for sound.** If the user likes acoustic music, acoustic songs score higher. If not, electronic songs score higher.

Then it sorts the songs from highest to lowest score. It shows the top 5. Each pick lists its reasons, like "genre match: pop (+2.0)."

**Changes from the starter:** The starter just returned the first few songs in the file. I added the CSV loader, the scoring checklist, the sorting, and the reasons.

---

## 4. Data  

- **18 songs.** The starter had 10, and I added 8.
- **15 genres and 14 moods.** My 8 songs added new genres like hip hop, metal, folk, and reggae. They also added new moods like sad, angry, and romantic.
- **Each song has** a genre, a mood, and five numbers. The numbers are energy, tempo, valence (how happy it sounds), danceability, and acousticness. Only genre, mood, energy, and acousticness count toward the score.
- **Limits:**
  - The catalog is uneven. Lofi has 3 songs and pop has 2, but most genres have just 1.
  - Two artists (Neon Echo and LoRoom) appear twice each.
  - Everything is made up.
  - There are no lyrics, languages, release years, popularity numbers, or listening history.

---

## 5. Strengths  

- **Different users get different lists.** Chill Lofi and Deep Intense Rock had zero songs in common.
- **A full match lands at #1.** Sunrise City (pop), Library Rain (lofi), and Storm Runner (rock) all scored above 4.8.
- **Energy rewards closeness.** A calm listener gets calm songs, not just the quietest one.
- **Every pick explains itself.** The reasons are how I found the capitalization bug and the Gym Hero pattern.

---

## 6. Limitations and Bias 

The system trusts text labels more than how a song sounds. Genre and mood are worth 3 of the 5 points, but only when the words match exactly. So "indie pop" earns nothing from a pop fan, and "Pop" with a capital P earns nothing at all. Lofi fans have three genre matches, but metal and folk fans have only one. In one test, a user who wanted high energy got a quiet folk song at #1 just because its labels matched.

---

## 7. Evaluation  

### Profiles tested

| Profile | genre / mood / energy / likes_acoustic | What it tests |
|---|---|---|
| High-Energy Pop | pop / happy / 0.8 / no | Typical listener (the default) |
| Chill Lofi | lofi / chill / 0.4 / yes | Typical listener, opposite end of the energy scale |
| Deep Intense Rock | rock / intense / 0.9 / no | Typical listener, genre with only one song |
| Sad but Hyped | folk / sad / 0.9 / no | Conflicting wishes: a sad, acoustic-style genre but high energy |
| Missing Genre | k-pop / happy / 0.5 / yes | A genre that isn't in the catalog at all |
| Capitalized Input | Pop / Happy / 0.8 / no | Same as High-Energy Pop, just typed with capital letters |

For each one, I checked three things. Did the #1 song make sense? Did the top 5 change when the profile changed? Did the reasons explain the score?

### Results

**High-Energy Pop**
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

**Chill Lofi**
```
=== Chill Lofi ===
Profile: genre=lofi, mood=chill, energy=0.4, likes_acoustic=True

1. Library Rain by Paper Lanterns  [4.85]
     - genre match: lofi (+2.0)
     - mood match: chill (+1.0)
     - energy 0.35 vs target 0.40 (+1.42)
     - acoustic fit (+0.43)
2. Midnight Coding by LoRoom  [4.82]
     - genre match: lofi (+2.0)
     - mood match: chill (+1.0)
     - energy 0.42 vs target 0.40 (+1.47)
     - acoustic fit (+0.35)
3. Focus Flow by LoRoom  [3.89]
     - genre match: lofi (+2.0)
     - energy 0.40 vs target 0.40 (+1.50)
     - acoustic fit (+0.39)
4. Spacewalk Thoughts by Orbit Bloom  [2.78]
     - mood match: chill (+1.0)
     - energy 0.28 vs target 0.40 (+1.32)
     - acoustic fit (+0.46)
5. Coffee Shop Stories by Slow Stereo  [1.90]
     - energy 0.37 vs target 0.40 (+1.46)
     - acoustic fit (+0.45)
```

**Deep Intense Rock**
```
=== Deep Intense Rock ===
Profile: genre=rock, mood=intense, energy=0.9, likes_acoustic=False

1. Storm Runner by Voltline  [4.93]
     - genre match: rock (+2.0)
     - mood match: intense (+1.0)
     - energy 0.91 vs target 0.90 (+1.48)
     - acoustic fit (+0.45)
2. Gym Hero by Max Pulse  [2.93]
     - mood match: intense (+1.0)
     - energy 0.93 vs target 0.90 (+1.46)
     - acoustic fit (+0.47)
3. Pulse Reactor by Kilowatt Kids  [1.92]
     - energy 0.95 vs target 0.90 (+1.43)
     - acoustic fit (+0.49)
4. Iron Cathedral by Grave Signal  [1.88]
     - energy 0.97 vs target 0.90 (+1.40)
     - acoustic fit (+0.48)
5. Sunrise City by Neon Echo  [1.79]
     - energy 0.82 vs target 0.90 (+1.38)
     - acoustic fit (+0.41)
```

**Sad but Hyped (conflicting)**
```
=== Sad but Hyped (conflicting) ===
Profile: genre=folk, mood=sad, energy=0.9, likes_acoustic=False

1. Paper Boats by Hollow Pines  [3.65]
     - genre match: folk (+2.0)
     - mood match: sad (+1.0)
     - energy 0.30 vs target 0.90 (+0.60)
     - acoustic fit (+0.05)
2. Storm Runner by Voltline  [1.93]
     - energy 0.91 vs target 0.90 (+1.48)
     - acoustic fit (+0.45)
3. Gym Hero by Max Pulse  [1.93]
     - energy 0.93 vs target 0.90 (+1.46)
     - acoustic fit (+0.47)
4. Pulse Reactor by Kilowatt Kids  [1.92]
     - energy 0.95 vs target 0.90 (+1.43)
     - acoustic fit (+0.49)
5. Iron Cathedral by Grave Signal  [1.88]
     - energy 0.97 vs target 0.90 (+1.40)
     - acoustic fit (+0.48)
```

**Missing Genre (k-pop)**
```
=== Missing Genre (k-pop) ===
Profile: genre=k-pop, mood=happy, energy=0.5, likes_acoustic=True

1. Rooftop Lights by Indigo Parade  [2.28]
     - mood match: happy (+1.0)
     - energy 0.76 vs target 0.50 (+1.11)
     - acoustic fit (+0.17)
2. Sunrise City by Neon Echo  [2.11]
     - mood match: happy (+1.0)
     - energy 0.82 vs target 0.50 (+1.02)
     - acoustic fit (+0.09)
3. Dusty Porch Swing by Willow Hollow  [1.84]
     - energy 0.52 vs target 0.50 (+1.47)
     - acoustic fit (+0.37)
4. Coffee Shop Stories by Slow Stereo  [1.75]
     - energy 0.37 vs target 0.50 (+1.30)
     - acoustic fit (+0.45)
5. Focus Flow by LoRoom  [1.74]
     - energy 0.40 vs target 0.50 (+1.35)
     - acoustic fit (+0.39)
```

**Capitalized Input (Pop/Happy)**
```
=== Capitalized Input (Pop/Happy) ===
Profile: genre=Pop, mood=Happy, energy=0.8, likes_acoustic=False

1. Concrete Verses by Blockwise  [1.93]
     - energy 0.78 vs target 0.80 (+1.47)
     - acoustic fit (+0.46)
2. Sunrise City by Neon Echo  [1.88]
     - energy 0.82 vs target 0.80 (+1.47)
     - acoustic fit (+0.41)
3. Night Drive Loop by Neon Echo  [1.81]
     - energy 0.75 vs target 0.80 (+1.42)
     - acoustic fit (+0.39)
4. Storm Runner by Voltline  [1.78]
     - energy 0.91 vs target 0.80 (+1.33)
     - acoustic fit (+0.45)
5. Gym Hero by Max Pulse  [1.78]
     - energy 0.93 vs target 0.80 (+1.30)
     - acoustic fit (+0.47)
```

### Do the results feel right?

Mostly. For High-Energy Pop, Sunrise City at #1 is exactly what I'd pick. It's the only song that's pop, happy, and at the right energy. Gym Hero at #2 feels a little off. It's a workout song. Rooftop Lights is happier and has almost the same energy, so I'd want it next.

**Why does Gym Hero keep showing up?** It shows up in 4 of the 6 lists. Think of the score as a checklist. Gym Hero is labeled "pop," so a pop fan gives it 2 points right away. That happens even though its mood is "intense," not "happy." It's also one of the loudest, least acoustic songs. So anyone who wants loud, non-acoustic music gives it high marks too. Rooftop Lights is the happier song. But its label says "indie pop," not "pop," so it misses the biggest item. That leaves it 1 point behind.

### What surprised me

- **Capital letters break everything.** To the program, "Pop" and "pop" are different words. So the Capitalized Input profile got no genre or mood points. Its list was just sorted by energy.
- **Labels win over sound.** The Sad but Hyped user got a slow, quiet folk song at #1. The next four were loud rock, pop, EDM, and metal songs. None of them were sad.
- **No warning for a missing genre.** There's no k-pop in the catalog, but the user was never told. The system just used mood and energy instead. It even put a country song at #3.

### Comparing profiles

- **High-Energy Pop vs. Chill Lofi:** The lists share no songs. Pop's picks are loud (energy 0.75–0.93). Lofi's picks are quiet (0.28–0.42) and acoustic. That makes sense, since the two profiles differ on every setting.
- **Chill Lofi vs. Deep Intense Rock:** These are also totally different. So yes, the system can tell chill lofi from intense rock.
- **High-Energy Pop vs. Deep Intense Rock:** Both lists include Gym Hero and Sunrise City. Both users want loud, non-acoustic music. Each user only has one or two genre matches. After those, the same loud songs fill both lists.
- **Deep Intense Rock vs. Sad but Hyped:** Spots 2–5 are almost the same: Storm Runner, Gym Hero, Pulse Reactor, and Iron Cathedral. Both profiles want 0.9 energy and no acoustic sound. "Folk/sad" only matched one song. So energy picked the rest.
- **High-Energy Pop vs. Capitalized Input:** This is the same request, just with capital letters. Sunrise City dropped from 4.88 to 1.88. Rooftop Lights fell out of the top 5. The user's taste didn't change, so this is a bug.
- **High-Energy Pop vs. Missing Genre (k-pop):** The k-pop list starts with the two happy songs, Rooftop Lights and Sunrise City. Both are in the pop list too. After that, the k-pop list moves to calmer, acoustic songs. That fits, since this user wants 0.5 energy and likes acoustic music. But a country song at #3 shows the system doesn't know which genres are similar.

### Experiment: weight shift (genre 2.0 → 1.0, energy 1.5 → 3.0)

I halved the genre weight and doubled the energy weight. The top possible score went from 5 to 5.5. Energy points stayed between 0 and 3, so the math still worked.

| Profile | Top 5 before | Top 5 after |
|---|---|---|
| High-Energy Pop | Sunrise City, Gym Hero, Rooftop Lights, Concrete Verses, Night Drive Loop | Sunrise City, **Rooftop Lights, Gym Hero**, Concrete Verses, Night Drive Loop |
| Chill Lofi | Library Rain, Midnight Coding, Focus Flow, Spacewalk Thoughts, Coffee Shop Stories | **Midnight Coding, Library Rain**, Focus Flow, Spacewalk Thoughts, Coffee Shop Stories |
| Deep Intense Rock | *(no change)* | *(no change)* |
| Sad but Hyped | Paper Boats, Storm Runner, Gym Hero, Pulse Reactor, Iron Cathedral | **Storm Runner, Gym Hero, Pulse Reactor, Iron Cathedral, Paper Boats** |
| Missing Genre (k-pop) | Rooftop Lights, Sunrise City, Dusty Porch Swing, Coffee Shop Stories, Focus Flow | Rooftop Lights, **Dusty Porch Swing, Sunrise City, Midnight Coding**, Focus Flow |

**Verdict: different, not clearly better.** It helped the pop fan, since Rooftop Lights passed Gym Hero. It gave the Sad but Hyped user high-energy songs. But it hurt the k-pop fan, who got a country song at #2. Lofi and rock barely changed. So I kept the original weights.

---

## 8. Future Work  

1. **Make matching forgiving.** Lowercase all text. Give partial credit for close labels, like "indie pop" and "pop." Warn users when their genre isn't in the catalog.
2. **Add variety to the top 5.** For example, allow only one song per artist. Then loud-music fans won't all get the same songs.
3. **Use more of the data.** Valence measures how happy a song sounds. A "sad" user could get low-valence songs even without a mood match. Users should also be able to say what they don't want.

---

## 9. Personal Reflection  

**Biggest learning moment:** The capitalization test. Typing "Pop" instead of "pop" dropped Sunrise City from 4.88 to 1.88. The math was fine. The input just wasn't what the code expected. Real systems need clean data, not just a good formula.

**Using AI tools:** AI helped me research how apps like Spotify recommend music. It also made new songs, wrote code fast, and ran the weight experiment. But I still had to check its work. I ran the code myself to check the scores.

**What surprised me:** Four simple rules already *feel* like real recommendations. Sunrise City at #1 for a pop fan looks smart. But it's just a checklist. Real apps might seem smarter than they are. A list can look confident and still have problems, like Gym Hero showing up for almost everyone.

**What I'd try next:** First, I'd fix the matching problems and add a variety rule. Then I'd add fake listening history for a few users. That would let me test "people like you also liked" and see how it changes the results.
