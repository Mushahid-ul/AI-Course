def dls(node,goal,depth_limit,graph,level = 0):
    print(f"visiting node {node} found at depth {level}")

    if node == goal:
        print(f"goal {goal} found at depth {level}")
        return True
    if level >= depth_limit:
        return False
    for child in graph.get(node,[]):
        if dls(child,goal,depth_limit,graph,level +1):
            return True
    return False

def ids(start,goal,max_limit,graph):
    for depth in range(max_limit + 1):
        print(f"\n trying depth limit {depth}")
        if dls(start,goal,depth,graph):
            print(f"goal {goal} found at depth limit{depth}")
            return True
    print(f"goal {goal} not found at max_limit{max_limit}")
    return False        

graph = {}

n = int(input("enter the number of nodes: "))

for i in range(n):
    node = input("enter the node number/name: ")
    neighbours = input(f"the neighbours of {node}: ").split()
    graph[node] = neighbours

start_node = input("enter the start node: ")
goal_node = input("enter the goal node: ")
max_limit = int(input("enter the max limit: "))

ids(start_node,goal_node,max_limit,graph)