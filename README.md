# Guess the Number Game

This is a simple Python-based game where the player attempts to guess a randomly chosen number between 1 and 100. The player is given a number of attempts based on their chosen difficulty (easy or hard) and receives feedback on whether their guess is too high or too low.

## Features:
- **Random Number Generation**: The program randomly selects a number between 1 and 100.
- **Difficulty Levels**: The player can choose between easy or hard difficulty, affecting the number of attempts available.
  - **Easy**: 10 attempts
  - **Hard**: 5 attempts
- **Feedback**: The player receives feedback after each guess, indicating whether the guess is too high, too low, or correct.
- **Game Continuation**: The game allows the player to play multiple rounds without restarting the program.

## How to Play:
1. The game prompts you to choose a difficulty level (either easy or hard).
2. The program selects a random number between 1 and 100.
3. The player has a limited number of attempts to guess the correct number.
4. After each guess, the program will tell you whether your guess is too high, too low, or correct.
5. The game ends when you either guess the number correctly or run out of attempts.
6. You can choose to play another round or exit the game.

## Installation:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ulquiorraexe/guess-the-number.git
   cd guess-the-number

2. **Run the game:**

   ```bash
   python main.py

3. Follow the prompts in the terminal to start playing the game.

## Game Rules

  - **Easy Mode:** You have 10 attempts to guess the number.
  - **Hard Mode:** You have 5 attempts to guess the number.
  - **Feedback:** After each guess, the program will indicate whether your guess was too high or too low.
  - **Winning:** If you guess the correct number, you win.
  - **Losing:** If you run out of attempts, you lose the game.

## Example Output

```swift
Welcome! Do you want to play? Type 'y' or 'n': y
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts to guess.
Make a guess: 50
Too low.
Guess again.
You have 9 attempts to guess.
Make a guess: 75
Too high.
Guess again.
You have 8 attempts to guess.
Make a guess: 60
You've won!
```

## License

This project does not have a license.
