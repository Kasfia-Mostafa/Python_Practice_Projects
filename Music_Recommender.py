import random

print("Music Recommender")

genre = {
    "rock": ["AC/DC", "Queen", "Led Zeppelin"],
    "pop": ["Taylor Swift", "Ed Sheeran", "Arina Grande"],
    "hip-hop": ["Kendrick", "Drake", "J.Cole"],
}

choice = input("What genre do you like ?")

if choice not in genre:
    print("Sorry I don't know that.")
else:
    print(f"Check out {random.choice(genre[choice])}")
