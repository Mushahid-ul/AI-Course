# Alpha-Beta Pruning with Optimal Path

Alpha-Beta Pruning is an optimization technique for the **Minimax algorithm** used in two-player games such as Chess, Tic-Tac-Toe, and Nim.  
It reduces the number of nodes evaluated in the game tree by pruning branches that cannot influence the final decision — making the search faster and more efficient.

## 1. How it Works
- Start from the root node and recursively explore child nodes.  
- Maintain two values:  
  - **Alpha (α):** The best score the maximizing player can guarantee.  
  - **Beta (β):** The best score the minimizing player can guarantee.  
- During traversal:
  - If **β ≤ α**, prune (skip) the remaining branches.  
- Continue until reaching leaf nodes.  
- Return the **best achievable value** and the **optimal path** from root to leaf.

## 2. Source Code
- **File:** [Alpha_Beta_Pruning.py](./Alpha_beta_proning.py)  
- **Language:** Python 3.x  

## 3. Applications
- Game AI (e.g., Chess, Tic-Tac-Toe, Checkers)  
- Decision-making in adversarial systems  
- Optimization and search problems with large state spaces  
- Used as a foundation in AI strategies and computer game engines  

## 4. Complexity
- **Time Complexity:** O(b^d) in the worst case, reduced significantly by pruning.  
  - *b = branching factor*  
  - *d = depth of the tree*  
- **Space Complexity:** O(b × d) due to recursion and node tracking.  


## 5. How to Run
```bash
python3 Alpha_Beta_Proning.py
# or
python Alpha_Beta_Proning.py


