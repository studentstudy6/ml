from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

# Taking nodes
for i in range(n):
    node = input("Enter node: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

# Taking edges
for i in range(e):
    u = input("Enter first node: ")
    v = input("Enter second node: ")

    if u in graph and v in graph:
        graph[u].append(v)
        graph[v].append(u)
    else:
        print("Invalid edge!")

start = input("Enter starting node: ")
goal = input("Enter goal node: ")

# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None

# DFS
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(path + [neighbour])

    return None

# Calling functions
if start in graph and goal in graph:
    bfs_path = bfs(graph, start, goal)
    dfs_path = dfs(graph, start, goal)

    print("\nBFS Path:", bfs_path)
    print("DFS Path:", dfs_path)

    if bfs_path:
        print("BFS Path Length:", len(bfs_path) - 1)

    if dfs_path:
        print("DFS Path Length:", len(dfs_path) - 1)
else:
    print("Invalid starting or goal node!")
5
