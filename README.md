# Tic-Tac-Toe AI

This project implements a Tic-Tac-Toe game where a human player can play against an AI opponent. The AI uses the minimax algorithm to determine the optimal move.

## Files

*   `tictactoe.py`: Contains all the core game logic, including functions to:
    *   Determine the current player.
    *   Get available actions on the board.
    *   Calculate the result of an action.
    *   Check for a winner.
    *   Determine if the game is over (terminal state).
    *   Calculate the utility of a terminal board.
    *   Implement the minimax algorithm to find the optimal move for the AI.
*   `runner.py`: Uses the Pygame library to create a graphical user interface (GUI) for the game. It handles user input, displays the game board, and manages the game flow between the human player and the AI.
*   `OpenSans-Regular.ttf`: The font file used for text rendering in the game.

## Requirements

*   Python 3
*   Pygame library

## How to Run

1.  **Ensure Python 3 is installed.**
2.  **Install Pygame:**
    If you don't have Pygame installed, you can install it using pip:
    ```bash
    pip install pygame
    ```
3.  **Download the project files:**
    Make sure `tictactoe.py`, `runner.py`, and `OpenSans-Regular.ttf` are in the same directory.
4.  **Run the game:**
    Open a terminal or command prompt, navigate to the directory containing the files, and run:
    ```bash
    python runner.py
    ```

## Gameplay

1.  When the game starts, you will be prompted to choose whether you want to play as 'X' or 'O'.
2.  Player 'X' always makes the first move.
3.  Click on an empty square on the board to make your move when it's your turn.
4.  The AI will automatically make its move when it is its turn.
5.  The game ends when one player gets three in a row (horizontally, vertically, or diagonally) or when all squares are filled, resulting in a tie.
6.  After a game ends, you will have the option to "Play Again".

## AI Opponent

The AI opponent uses the **minimax algorithm** to play optimally. This means that if you also play optimally, the game will always result in a tie. You should not be able to beat the AI; however, if you make a suboptimal move, the AI may be able to win.

Enjoy the game! 