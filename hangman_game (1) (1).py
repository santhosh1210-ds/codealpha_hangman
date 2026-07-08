import random

# ============================================
#   HANGMAN GAME - CodeAlpha Internship Task 1
#   Author: Dharshini
# ============================================

# 5 predefined words (as per task requirement)
WORDS = ["python", "coding", "github", "intern", "laptop"]

# Hangman ASCII art stages (0 = start, 6 = dead)
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========="""
]

def display_board(wrong_guesses, guessed_letters, word):
    """Display hangman, guessed letters, and word progress."""
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\n  Wrong guesses left: {6 - wrong_guesses}")
    print(f"  Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    # Show word with blanks
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\n  Word: {display_word}\n")

def play_hangman():
    """Main game function."""
    print("\n" + "="*40)
    print("       🎮 HANGMAN GAME 🎮")
    print("       CodeAlpha Internship - Task 1")
    print("="*40)
    
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print(f"\n  Guess the word! It has {len(word)} letters.")
    print("  You have 6 chances.\n")

    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, guessed_letters, word)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"  🎉 You WON! The word was: '{word.upper()}'")
            break

        # Get player input
        guess = input("  Enter a letter: ").lower().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠️  Please enter a single letter only!\n")
            continue

        if guess in guessed_letters:
            print(f"  ⚠️  You already guessed '{guess}'. Try another!\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"  ❌ Wrong! '{guess}' is not in the word. ({6 - wrong_guesses} chances left)\n")

    else:
        # Game over
        display_board(wrong_guesses, guessed_letters, word)
        print(f"  💀 Game Over! The word was: '{word.upper()}'")

    print("\n" + "="*40)

def main():
    while True:
        play_hangman()
        again = input("\n  Play again? (yes/no): ").lower().strip()
        if again not in ["yes", "y"]:
            print("\n  Thanks for playing! 👋\n")
            break

if __name__ == "__main__":
    main()