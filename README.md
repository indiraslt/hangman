# hangman


---

# Hangman Game

This is a terminal-based implementation of the classic Hangman game, written in Python. Players can guess letters one by one or attempt to guess the entire word.

## Features
- Random word selection from a predefined list.
- Display of the word with hidden letters (`_`) until they are guessed.
- Visual representation of the "hanging man" that changes based on the remaining tries.
- Ability to guess individual letters or the full word.
- Automatic tracking of incorrect guesses.

---

## Requirements
- Python 3.x (latest version recommended)
- No additional Python modules are required (uses only the standard library).

---

## Installation
1. Download or clone the project files.
2. Open a terminal and ensure Python is installed (use `python --version` or `python3 --version` to check).
3. Open the project in a Python IDE (e.g., PyCharm) or prepare to run it directly from the terminal.

---

## How to Run
1. Open your terminal or Python IDE.
2. Run the following command:
   ```bash
   python hangman.py
   ```
3. Follow the on-screen instructions to play the game.

---

## How to Play
- Guess letters or try to guess the entire word.
- For each incorrect guess, you lose a life.
- The game ends when:
  - You correctly guess the word.
  - You lose all your lives.

---

## File Structure
- **hangman.py**: The main game file.
- **README.md**: Documentation for the project.

---

## Customizing the Game
### Adding or Removing Words
1. Open the `hangman.py` file.
2. Edit the word list:
   ```python
   WORDS = ['apple', 'banana', 'grape', 'orange', 'kiwi']
   ```

### Changing the Number of Tries
1. Locate the following line:
   ```python
   tries = 6
   ```
2. Replace `6` with the desired number of tries.

---

## License
This project is open-source and intended for educational purposes. Feel free to modify and share it as needed.

---

## Author
Created by [Indiras Ramanauskas]  
Contact: [indiraslt@yahoo.com]

---

This `README.md` provides users with a clear guide on how to run, play, and customize the Hangman game.