"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""


import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_profiles = [
        {"name": "High-Energy Pop", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9}},
        {"name": "Chill Lofi", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.3}},
        {"name": "Deep Intense Rock", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95}},
        {"name": "Conflicted Edge Case", "prefs": {"genre": "jazz", "mood": "sad", "energy": 0.9}},
    ]

    for profile in user_profiles:
        print(f"\nTop recommendations for {profile['name']} profile:\n")
        recommendations = recommend_songs(profile['prefs'], songs, k=5)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
