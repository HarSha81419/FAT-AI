from collections import deque

nodes = input("Enter the nodes (space separated): ").split()

e = int(input("Enter the number of edges: "))

graph = {node: [] for node in nodes}

print(graph)

print("Enter the edges (in format u, v): ")
edges = []

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
    edges.append((u,v))

print("Edges entered: ")
for edge in edges:
    print(edge)

print(graph)

start = input("Enter the start node: ")

def dfs(graph, start, visited = None, path = None):
    if visited == None:
        visited = set()
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    
    return path

dfs_result = dfs(graph, start)
print("Final DFS path: ", dfs_result)