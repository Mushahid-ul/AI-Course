nodes = input("Enter all nodes: ").split()
graph = {}
for node in nodes:
    graph[node] = input(f"Enter neighbors of {node} (leave blank if none): ").split()

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Best-First Search

def best_first_search(graph, start, goal, heuristic):
    open = [(start, [start])]
    visited = set()

    while open:
        # Pick node with smallest heuristic
        current_node, path = min(open, key=lambda x: heuristic[x[0]])
        open.remove((current_node, path))

        if current_node in visited:
            continue
        visited.add(current_node)

        print("Visiting:", current_node)

        if current_node == goal:
            print("Goal found:", current_node)
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                open.append((neighbor, path + [neighbor]))

    print("Goal not reachable.")

# Run the search
print("\n--- Best First Search ---")
best_first_search(graph, start, goal, heuristic)
