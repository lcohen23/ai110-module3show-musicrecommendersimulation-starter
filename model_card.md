# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The system's biggest weakness is that it trusts text labels more than how a song actually sounds. Genre and mood together are worth 3 of the 5 possible points, and they only count when the words match exactly, so "indie pop" earns nothing from a pop fan, and typing "Pop" instead of "pop" wipes out every label point (Sunrise City fell from 4.88 to 1.88). This creates an uneven filter bubble: lofi fans have three songs that can earn the genre bonus, while folk, metal, or classical fans have only one, so after their first pick they just get whatever songs happen to have a similar energy level. In the "Sad but Hyped" test, the label bonus was strong enough to put Paper Boats (energy 0.30) at #1 for a user who asked for 0.90 energy, which shows that a label match can override what the user said about energy.

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

For each one I checked whether the #1 song made sense, whether the top 5 changed when the profile changed, and whether the listed reasons explained the score.

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

Mostly. For High-Energy Pop, Sunrise City at #1 is exactly what I'd pick: it's the only song that's pop, happy, and at the right energy. Gym Hero at #2 feels a little off, though. It's a workout track, and Rooftop Lights (happy, nearly the same energy) is the song I'd actually want next.

**Why does Gym Hero keep showing up?** It appears in 4 of the 6 lists. Think of the score as a checklist. Gym Hero is labeled "pop," so a pop fan gives it 2 points right away, even though its mood is "intense" rather than "happy." It is also one of the loudest, least acoustic songs in the catalog, so anyone who wants high energy and doesn't want acoustic music gives it almost full marks on those two items as well. Rooftop Lights is the happier song, but because its label says "indie pop" instead of "pop," it misses the biggest item on the checklist and ends up 1 point behind.

### What surprised me

- **Capital letters break everything.** "Pop" and "pop" are different words to the program, so the Capitalized Input profile got no genre or mood points at all, and its list turned into a plain sort by energy.
- **Conflicting wishes are settled by labels, not sound.** The Sad but Hyped user got a slow, quiet folk song at #1, followed by four loud rock, pop, EDM, and metal songs, none of them sad.
- **No warning for a missing genre.** The k-pop user was never told that there's no k-pop in the catalog. The system quietly fell back to mood and energy and even put a country song in 3rd place.

### Comparing profiles

- **High-Energy Pop vs. Chill Lofi:** The two lists have no songs in common. Pop's picks are loud (energy 0.75–0.93) and produced, while lofi's are quiet (0.28–0.42) and acoustic. That makes sense because the two profiles disagree on every setting.
- **Chill Lofi vs. Deep Intense Rock:** These are also completely different, which answers the Phase 2 question: yes, the system can tell "chill lofi" apart from "intense rock."
- **High-Energy Pop vs. Deep Intense Rock:** Both lists include Gym Hero and Sunrise City. Both users want loud, non-acoustic music, so once each user's single genre match is used up, the remaining spots go to the same loud songs.
- **Deep Intense Rock vs. Sad but Hyped:** Places 2–5 are nearly identical (Storm Runner, Gym Hero, Pulse Reactor, Iron Cathedral). Both profiles ask for 0.9 energy and non-acoustic music, and "folk/sad" matched only one song, so the energy setting chose everything else.
- **High-Energy Pop vs. Capitalized Input:** These are the same request, but Sunrise City dropped from 4.88 to 1.88 and Rooftop Lights fell out of the top 5. Nothing about the user's taste changed, so this is a bug, not a difference in preference.
- **High-Energy Pop vs. Missing Genre (k-pop):** Both lists start with the happy songs (Sunrise City and Rooftop Lights). After that, the k-pop list moves toward calmer, acoustic songs because the user asked for 0.5 energy and likes acoustic music. That's reasonable, but a country song at #3 shows the system has no idea which genres are "close" to each other.

### Experiment: weight shift (genre 2.0 → 1.0, energy 1.5 → 3.0)

I halved the genre weight and doubled the energy weight. The highest possible score became 5.5, and every energy score stayed between 0 and 3.

| Profile | Top 5 before | Top 5 after |
|---|---|---|
| High-Energy Pop | Sunrise City, Gym Hero, Rooftop Lights, Concrete Verses, Night Drive Loop | Sunrise City, **Rooftop Lights, Gym Hero**, Concrete Verses, Night Drive Loop |
| Chill Lofi | Library Rain, Midnight Coding, Focus Flow, Spacewalk Thoughts, Coffee Shop Stories | **Midnight Coding, Library Rain**, Focus Flow, Spacewalk Thoughts, Coffee Shop Stories |
| Deep Intense Rock | *(no change)* | *(no change)* |
| Sad but Hyped | Paper Boats, Storm Runner, Gym Hero, Pulse Reactor, Iron Cathedral | **Storm Runner, Gym Hero, Pulse Reactor, Iron Cathedral, Paper Boats** |
| Missing Genre (k-pop) | Rooftop Lights, Sunrise City, Dusty Porch Swing, Coffee Shop Stories, Focus Flow | Rooftop Lights, **Dusty Porch Swing, Sunrise City, Midnight Coding**, Focus Flow |

**Verdict: different, not clearly better.** It helped High-Energy Pop: Rooftop Lights finally moved ahead of Gym Hero. It also made Sad but Hyped respect the energy request. But it hurt the k-pop user, who now gets a country song at #2. Lofi and rock barely changed. Because the results were mixed, I kept the original weights.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
