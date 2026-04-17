from collections import deque

nodes = input("Enter the nodes (space separated): ").split()

graph = {node : [] for node in nodes}

e = int(input("Enter the number of edges: "))
edges = []

print("Enter the edges (in format u v): ")

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
    edges.append((u, v))

def dls(graph, current, goal, depth, path, visited):
    print(f"Visiting {current}, Depth left: {depth}")

    if current == goal:
        print(f"Found goal at depth: {depth}")
        return True
    
    if depth <= 0:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            path.append(neighbor)
            if dls(graph, neighbor, goal, depth - 1, path, visited):
                return True
            path.pop()
    
    return False

start = input("Enter the Start node: ")
goal = input("Enter the goal node: ")
max_depth = int(input("Enter the max depth: "))
path = [start]
visited = set()

result = dls(graph, start, goal, max_depth, path, visited)

if result:
    print("Path: ", path)
else:
    print("Goal not Found")