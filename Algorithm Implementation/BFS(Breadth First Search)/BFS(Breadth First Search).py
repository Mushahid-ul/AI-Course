#BFS
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name/number: ")
    neighbours = input(f"Enter neighbours of {node} : ").split()
    graph[node] = neighbours

visited = []  
queue = []    

def bfs(visited, graph, node):  
    visited.append(node)
    queue.append(node)

    while queue:  
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("The Breadth-First Search is:")

start = input("Enter starting node: ")

bfs(visited, graph, start)  