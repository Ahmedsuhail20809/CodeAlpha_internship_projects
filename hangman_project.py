#Task 01: Hangman Game----

import random

# let's crate list of words for game, each word has 5 letters
word_list = ["apple", "house", "tiger", "chair", "plant"]

# Randomly select a word from the list
secret_word = random.choice(word_list)

# Create a list with underscores for each letter in the word (e.g., "_ _ _ _ _")
guessed_word = ["_" for _ in secret_word]

# Track the letters guessed and number of incorrect attempts
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Game loop
while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("\nCurrent word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print(f"Remaining attempts: {max_incorrect - incorrect_guesses}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1: # check if the guess is a single alphabetic character
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess.")
        incorrect_guesses += 1

# Final Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over! The correct word was:", secret_word)

print("Thanks for playing!")
