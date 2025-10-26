def dls(node, goal, depth_limit, graph, level=0):
    print(f"Visiting node {node} at depth {level}")

    if node == goal:
        print(f"Goal {goal} found at depth {level}")
        return True

    if level >= depth_limit:
        return False

    for child in graph.get(node, []):
        if dls(child, goal, depth_limit, graph, level + 1):
            return True
    return False


graph = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("Enter the node name: ")
    neighbours = input(f"The neighbours of {node}: ").split()
    graph[node] = neighbours

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
max_limit = int(input("Enter the max depth limit: "))

if not dls(start_node, goal_node, max_limit, graph):
    print("Goal not found within depth limit")
