# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  


This recommender suggests songs to users based on their stated preferences for genre, mood, and musical features like energy and tempo. It is designed for classroom exploration and learning, not for real-world deployment. The system assumes users can describe their musical taste in terms of a few key features.

---

## 3. How the Model Works  


The model looks at each song's genre, mood, energy, valence, danceability, tempo, and acousticness. It compares these to the user's favorite genre, mood, and target values for the other features. Songs get points for matching the user's genre and mood, and more points the closer they are to the user's preferred energy, tempo, etc. In my experiment, I doubled the importance of energy and reduced the weight of genre to see how it changed the results.

---

## 4. Data  


The dataset contains 20 songs with a variety of genres (pop, lofi, rock, jazz, synthwave, indie, world, electronic, folk, classical, country, blues, chiptune, reggae, trip hop) and moods (happy, chill, intense, relaxed, moody, focused, peaceful, upbeat, melancholic, playful, hopeful, reflective, energetic, calm, sad). I expanded the starter data to include more diversity. Some musical styles and modern subgenres are still missing.

---

## 5. Strengths  


The system works well for users with clear preferences, like those who want high-energy pop or chill lofi. It captures the "vibe" of a user profile and usually puts songs with matching genre and mood at the top. The recommendations generally matched my intuition for the test profiles.

---

## 6. Limitations and Bias 


The system can over-prioritize energy or genre depending on the weights, sometimes ignoring good matches in other features. If a genre or mood is rare in the dataset, those songs are less likely to be recommended. The system does not consider lyrics, artist popularity, or user history, and may create "filter bubbles" by always recommending the same style for a given profile.

---

## 7. Evaluation  


I tested the system with four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a Conflicted Edge Case. I checked if the top songs matched the intended vibe and if the explanations made sense. When I doubled the energy weight, the system started recommending more energetic songs even if the genre didn't match, showing how weights affect results. It was interesting to see how a single feature could dominate the ranking.

---

## 8. Future Work  


I would add more features (like lyrics, artist, or release year), improve the explanations, and add logic to increase diversity in the top results. Supporting more complex user profiles (multiple favorite genres, mood ranges) would make the system more flexible and realistic.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
