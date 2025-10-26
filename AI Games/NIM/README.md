# 🎮 NIM Game (Human vs AI using Minimax Algorithm)

## Overview
This is an **NIM Game built in Python (Tkinter)** where a **human player competes against an AI opponent**.  
The AI uses the **Minimax algorithm** to decide the optimal move and always tries to win, making the game challenging and educational.


## Algorithm Used
The game uses the **Minimax Algorithm** for the AI player.  
- The AI evaluates all possible moves recursively.  
- Each board state (number of stones in piles) is scored as:
  - `+1` for AI winning positions  
  - `-1` for player winning positions  
- The AI chooses moves that **maximize its chance to win** and **minimize the player’s chance**.


## How to Play
1. There are **3 piles** of stones: `[3, 4, 5]`.  
2. **Your turn:** Click the button under a pile to remove 1, 2, or more stones.  
3. **AI turn:** The AI calculates and removes stones automatically.  
4. The **player who takes the last stone loses** (standard misère NIM rules).  
5. Game ends when all stones are removed:
   - 🎉 Player wins  
   - 🤖 AI wins  

---

## How to Run the Game
1. Install **Python 3.x** on your system.  
2. Clone or download the repository:
   ```bash
   git clone https://github.com/mushahid_ul/AI-Course.git

3. Or just simply run it in VS Code
