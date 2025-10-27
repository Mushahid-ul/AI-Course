# Minimax Algorithm with Optimal Path

The **Minimax Algorithm** is a classic decision-making algorithm used in **two-player games** such as Chess, Tic-Tac-Toe, and Nim.  
It aims to minimize the possible loss in a worst-case scenario. When dealing with gains, it maximizes the minimum gain — hence the name **Minimax**.

This implementation also shows the **optimal path** from the root to the best leaf node based on the chosen player (Maximizer or Minimizer).

## 1. How It Works
- The algorithm recursively explores all possible moves (states) of a game tree.
- Two players alternate:
  - **Maximizing Player**: Tries to get the highest possible score.
  - **Minimizing Player**: Tries to get the lowest possible score.
- The recursion continues until reaching leaf nodes (final outcomes).
- The best value and corresponding path are selected for the starting player.

## 2. Source Code
- **File:** [Minimax_Algorithm.py](./Minmax_Algorithm.py)  
- **Language:** Python 3.x  

## 3. Applications
- Used in **Game AI** (Chess, Tic-Tac-Toe, Checkers, Nim, etc.)
- Decision making in **competitive or adversarial environments**
- **AI problem-solving** in two-agent systems
- Forms the foundation for **Alpha-Beta Pruning**

## 4. Complexity
- **Time Complexity:** O(b^d)  
  - *b = branching factor (number of moves per state)*  
  - *d = depth of the tree*  
- **Space Complexity:** O(b × d) — due to recursive call stack.


