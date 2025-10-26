
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name/number: ")
    neighbours = input(f"Enter neighbours of {node} : ").split()
    graph[node] = neighbours

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_visited = {start: None}
    back_visited = {goal: None}

    front_queue = [start]
    back_queue = [goal]

    while front_queue and back_queue:
        
        f = front_queue.pop(0)
        for neigh in graph[f]:
            if neigh not in front_visited:
                front_visited[neigh] = f
                front_queue.append(neigh)
                if neigh in back_visited:
                    print(f"Meeting point: {neigh}")  # Added line
                    return make_path(front_visited, back_visited, neigh)

        
        b = back_queue.pop(0)
        for neigh in graph[b]:
            if neigh not in back_visited:
                back_visited[neigh] = b
                back_queue.append(neigh)
                if neigh in front_visited:
                    print(f"Meeting point: {neigh}")  # Added line
                    return make_path(front_visited, back_visited, neigh)
    return None

def make_path(fv, bv, meet):
    path = []
    node = meet
    while node is not None:
        path.append(node)
        node = fv[node] 
    path.reverse()
    node = bv[meet]
    while node is not None:
        path.append(node)
        node = bv[node]
    return path


start = input("Enter starting node: ")
goal = input("Enter goal node: ")

res = bidirectional_search(graph, start, goal)
if res:
    print("Path found:", " -> ".join(res))
else:
    print("No path found!")