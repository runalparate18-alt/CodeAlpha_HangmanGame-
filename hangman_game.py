import random

# Words list
words = ["apple", "train", "python", "cricket", "laptop"]

# Random word select
word = random.choice(words).lower()

# Display setup
guessed_word = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower().strip()

    # ✅ VALIDATION (VERY IMPORTANT)
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter ONLY one letter (a-z)")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\n🎉 You WIN! Word was:", word)
else:
    print("\n💀 You LOSE! Word was:", word)