def a_star(start, goal, graph, h):
    open_list = [(start, [start], 0)]   # (node, path, g)

    while open_list:
        open_list.sort(key=lambda x: x[2] + h[x[0]])  # f = g+h
        node, path, g = open_list.pop(0)

        if node == goal:
            return path, g

        for neigh, cost in graph[node]:
            open_list.append((neigh, path + [neigh], g + cost))

    return None, float("inf")


# -------- USER INPUT --------
n = int(input("Number of nodes: "))

h = {}
graph = {}

print("\nEnter heuristic values:")
for _ in range(n):
    node = input("Node name: ")
    hv = int(input(f"Heuristic of {node}: "))
    h[node] = hv
    graph[node] = []

print("\nEnter neighbors (type 'done' to stop for a node):")
for node in graph:
    while True:
        neigh = input(f"Neighbor of {node} (or 'done'): ")
        if neigh == "done":
            break
        cost = int(input(f"Cost {node} → {neigh}: "))
        graph[node].append((neigh, cost))

start = input("\nStart node: ")
goal = input("Goal node: ")

path, cost = a_star(start, goal, graph, h)
print("\nShortest Path:", path)
print("Total Cost:", cost)
