import random

# List of words for the Hangman game
WORDS = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'melon', 'peach', 'plum', 'pear', 'carrot', 'daddy']


def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
    ]
    return stages[tries]


def hangman():
    print("Welcome to Hangman!")
    word = random.choice(WORDS).lower()
    word_completion = "_" * len(word)  # Underscores for each letter
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(f"Word: {word_completion}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Enter your guess (single letter or the whole word): ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries = tries - 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join(
                    guess if letter == guess else word_completion[i]
                    for i, letter in enumerate(word)
                )
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Try again.")

    print(display_hangman(tries))
    if guessed:
        print(f"Congratulations! You guessed the word: {word}!")
    else:
        print(f"Sorry, you ran out of tries. The word was: {word}.")


# Run the game
if __name__ == "__main__":
    hangman()
