# -----------------------------------------------
# 🌟 Alpha-Beta Pruning with Optimal Path
# -----------------------------------------------

def alphabeta(node, maximizing, tree, alpha, beta):
    """
    Alpha-Beta pruning algorithm that returns:
    - best value for current player (maximizing/minimizing)
    - optimal path from root to leaf
    """
    # Base case: leaf node (integer value)
    if not isinstance(tree[node], list):
        return tree[node], [node]

    if maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = alphabeta(child, False, tree, alpha, beta)
            if value > best_value:
                best_value = value
                best_path = [node] + path
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # pruning
        return best_value, best_path

    else:  # minimizing player
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = alphabeta(child, True, tree, alpha, beta)
            if value < best_value:
                best_value = value
                best_path = [node] + path
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # pruning
        return best_value, best_path


# --------------------------
# Step 1: Input tree structure
# --------------------------
tree = {}
n = int(input("Number of non-leaf nodes: "))

for _ in range(n):
    node = input("Node name: ").strip().upper()
    children = input(f"Children of {node} (comma separated): ").strip()
    tree[node] = [c.strip().upper() for c in children.split(',')]


# --------------------------
# Step 2: Input leaf node values
# --------------------------
for node in list(tree.keys()):
    for child in tree[node]:
        if child not in tree:  # leaf node
            value = int(input(f"Value of leaf node {child}: "))
            tree[child] = value


# --------------------------
# Step 3: Input root & starting player
# --------------------------
root = input("Root node: ").strip().upper()
start_player = input("Is maximizing player starting? (yes/no): ").strip().lower()
max_player = True if start_player == "yes" else False


# --------------------------
# Step 4: Run Alpha-Beta
# --------------------------
best_value, best_path = alphabeta(root, max_player, tree, float('-inf'), float('inf'))

# --------------------------
# Step 5: Display results
# --------------------------
print(f"\nBest value for {'maximizing' if max_player else 'minimizing'} player: {best_value}")
print(f"Optimal path: {' -> '.join(best_path)}")