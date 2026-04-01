from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and converts numerical fields to float/int.
    Returns a list of song dictionaries.
    """
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': int(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
    print(f"Loaded songs: {len(songs)}")
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    Scores and ranks all songs for the user. Returns top k as (song, score, explanation).
    """
    def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, list]:
        score = 0.0
        reasons = []
        # Genre match (weight halved)
        if 'genre' in user_prefs and song['genre'] == user_prefs['genre']:
            score += 1.0
            reasons.append('genre match (+1.0)')
        # Mood match
        if 'mood' in user_prefs and song['mood'] == user_prefs['mood']:
            score += 1.0
            reasons.append('mood match (+1.0)')
        # Energy similarity (weight doubled)
        if 'energy' in user_prefs:
            sim = 2 * (1 - abs(song['energy'] - user_prefs['energy']))
            score += sim
            reasons.append(f"energy similarity (+{sim:.2f})")
        # Valence similarity
        if 'valence' in user_prefs:
            sim = 1 - abs(song['valence'] - user_prefs['valence'])
            score += sim
            reasons.append(f"valence similarity (+{sim:.2f})")
        # Danceability similarity
        if 'danceability' in user_prefs:
            sim = 1 - abs(song['danceability'] - user_prefs['danceability'])
            score += sim
            reasons.append(f"danceability similarity (+{sim:.2f})")
        # Tempo similarity (normalize by 100 bpm range)
        if 'tempo_bpm' in user_prefs:
            sim = 1 - abs(song['tempo_bpm'] - user_prefs['tempo_bpm']) / 100.0
            sim = max(0, sim)
            score += sim
            reasons.append(f"tempo similarity (+{sim:.2f})")
        # Acousticness similarity
        if 'acousticness' in user_prefs:
            sim = 1 - abs(song['acousticness'] - user_prefs['acousticness'])
            score += sim
            reasons.append(f"acousticness similarity (+{sim:.2f})")
        return score, reasons

    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        results.append((song, score, explanation))
    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:k]
