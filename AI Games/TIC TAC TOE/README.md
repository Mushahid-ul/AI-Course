# 🎮 Tic Tac Toe (AI Game using Minimax Algorithm)

## Overview
This is a classic **Tic Tac Toe game** built with **Python (Tkinter)** where the player competes against an **AI opponent**.  
The AI is powered by the **Minimax algorithm**, which makes strategic moves to either win or force a draw, making it nearly unbeatable.


## Algorithm Used
The **Minimax algorithm** is a decision-making algorithm commonly used in two-player turn-based games such as Chess, Checkers, and Tic Tac Toe.  

It works by:
1. Exploring all possible future moves.
2. Assuming the opponent will also play optimally.
3. Choosing the move that maximizes its chances of winning (and minimizes the opponent’s chances).

The AI evaluates the board recursively until it finds the best move possible.


## How to Play
- You play as **X**, and the AI plays as **O**.
- Click on any empty box to place your move.
- The AI will automatically make its move after yours.
- The game declares **“X wins,” “O wins,”** or **“Tie!”** through a pop-up window.
- After each match, the game resets automatically for a new round.


## How to Run the Game
1. Install **Python 3.x** on your computer.
2. Make sure the **Tkinter library** is installed (comes pre-installed with Python).
3. Download or clone this repository:
   ```bash
   git clone https://github.com/Mushahid_ul/AI-Course.git

