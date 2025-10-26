print("Number of nodes:")
nodenumber = int(input())

graph = {}
print("Enter each node:")
nodes = []
for i in range(nodenumber):
    node = input()
    nodes.append(node)

for node in nodes:
    neighbors = input(f"Enter the neighbors of {node}: ").split()
    graph[node] = neighbors

heuristic = {}
for node in nodes:
    h = int(input(f"Enter the heuristic of {node}: "))
    heuristic[node] = h

print("Start node:")
start = input()

print("Goal node:")
goal = input()

print("Beam width:")
beam_width = int(input())

def beam_search(graph, heuristic, start, goal, beam_width):
    open = [[start]]
    while open:
        open = sorted(open, key=lambda p: heuristic[p[-1]])[:beam_width]
        next_open = []
        for current_path in open:
            node = current_path[-1]
            if node == goal:
                return current_path
            for neighbor in graph.get(node, []):
                if neighbor not in current_path:
                    next_open.append(current_path + [neighbor])
        open = next_open
    return None

result = beam_search(graph, heuristic, start, goal, beam_width)

if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found.")
