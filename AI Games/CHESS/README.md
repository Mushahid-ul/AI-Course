# Chess Game (Human vs AI)

## Overview

This project implements a **Chess game** where a human player plays as White against an AI opponent (Black). The AI uses the **Minimax algorithm** for decision-making, with an evaluation based on **material count**. The game includes a GUI built with **Tkinter**.

## Files in this folder

* `chesss.py`: Main Python source code.
* `input_output_screenshots/`: Folder containing gameplay screenshots.
* `README.md`: This file.

## How to Run

1. Ensure **Python 3.x** is installed on your system.
2. Install the required libraries:

```bash
pip install python-chess
```

3. Run the game:

```bash
python chess_minimax.py
```

## 🎮 How to Play

1. Click on a White piece to select it.
2. Click on a valid destination square to move the piece.
3. The AI will make its move automatically after yours.
4. The game ends when one side is checkmated or a draw occurs.
5. You can use the buttons to:

   * **Restart**: Reset the game.
   * **Pause/Resume**: Pause or resume the game.
   * **Level**: Change AI difficulty (Easy/Medium/Hard).

### Features

* Check/checkmate signal with blinking effect.
* Pawn promotion dialog.
* AI difficulty levels adjust the depth of Minimax.

## Algorithm Used

* **Minimax Algorithm**: AI evaluates all possible moves up to a depth limit and chooses the move with the optimal outcome.
* **Heuristic Evaluation**: Counts material value (pieces) to determine the board score.

| Piece  | Value | 
| ------ | ----- | 
| Pawn   | 1     |  
| Knight | 3     | 
| Bishop | 3     | 
| Rook   | 5     | 
| Queen  | 9     | 
| King   | 1000  | # High to prioritize safety |

---

## Screenshots

The folder `chess1.png, chess2.png, chess3.png ` contains images showing gameplay examples, check signals, and game-over scenarios.

---

## Features

* Human vs AI chess.
* AI uses Minimax with adjustable depth.
* Visual indicators for possible moves and captures.
* Check/checkmate signals with blinking effect.
* Simple and interactive GUI using Tkinter.

## Dependencies

* Python 3.x
* `tkinter` (usually comes pre-installed with Python)
* `python-chess` library

Install `python-chess` using:

```bash
pip install python-chess
```

---

## ✍️ Author

Created by: Mushahidul Islam
