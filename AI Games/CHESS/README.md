# ♟️ Chess Game (Human vs AI using Minimax Algorithm)

##  Overview
This is a **Chess Game built in Python (Tkinter)** where a **human player competes against an AI opponent**.  
The AI uses the **Minimax algorithm** to evaluate and play moves based on board strength — resulting in a smart, strategic opponent that adapts to your play style.


## 🧠 Algorithm Used
This project implements the **Minimax Algorithm** — a recursive, game-tree search technique that simulates all possible moves and counter-moves.  
It chooses the move that **maximizes its advantage** and **minimizes the player’s advantage**.

Each board position is **evaluated numerically** based on piece values:
- Pawn: 1  
- Knight: 3  
- Bishop: 3  
- Rook: 5  
- Queen: 9  
- King: 1000  

These values help the AI decide which move yields the strongest overall position.

## 🕹 How to Play
1. You (the player) control the **white pieces**.  
2. The **AI controls black**.  
3. Click a piece to select it — legal moves will be highlighted.  
4. Click again on a destination square to make your move.  
5. The AI automatically responds after your turn.  
6. The game declares results as:
   - ✅ *White Wins!*  
   - 🤖 *Black (AI) Wins!*  
   - 🤝 *Draw Game!*  
7. Use buttons for:
   - ♻ **Restart** – Start a new game  
   - ⏸ **Pause / Resume** – Pause or continue the game  
   - 🎯 **Level** – Change AI difficulty between *Easy*, *Medium*, and *Hard*

---

## How to Run the Game
1. Install **Python 3.x** on your system.  
2. Install the **chess** module (for board logic):
   ```bash
   pip install chess
```Run this in Terminal
    python chess_game.py

