def minimax(node, maximizing, tree):
    
    if isinstance(tree[node], int):
        return tree[node], [node]

    if maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, False, tree)
            if value > best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, True, tree)
            if value < best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path


# ------------ User Input ------------
tree = {}
n = int(input("Number of non-leaf nodes: "))

for _ in range(n):
    node = input("Node name: ").strip()
    children = input(f"Children of {node} (comma separated, leave blank if leaf): ").strip()
    if children:
        tree[node] = [c.strip() for c in children.split(',')]
    else:
        tree[node] = []

# Leaf node values input
for node in list(tree.keys()):
    for child in tree[node]:
        if child not in tree:  
            value = int(input(f"Value of leaf node {child}: "))
            tree[child] = value

# Root and player input
root = input("Root node: ").strip()
start_player = input("Is maximizing player starting? (yes/no): ").strip()
max_player = True if start_player == "yes" else False

# Run Minimax
value, path = minimax(root, max_player, tree)
print(f"Best value for {'maximizing' if max_player else 'minimizing'} player: {value}")
print(f"Optimal path: {' -> '.join(path)}")
