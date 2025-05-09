import random

print("Word Scrambler")

while True:
    word = input("\nEnter a word to scramble (or quit): ")
    if word.lower() == "quit":
        print("Goodbye")
        break

    letter = list(word)
    random.shuffle(letter)
    print(f"Scremabled: {"".join(letter)}")
