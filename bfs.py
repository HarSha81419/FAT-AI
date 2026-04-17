from collections import deque

# Input nodes
nodes = input("Enter nodes (space separated): ").split()

# Input number of edges
e = int(input("Enter number of edges: "))

# Initialize graph
graph = {node: [] for node in nodes}

print("Enter edges (format: u v):")
edges = []

# Input edges
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # Remove if directed
    edges.append((u, v))

# Print edges
print("\nEdges entered:")
for edge in edges:
    print(edge)

# -------- BFS --------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    bfs_path = []

    print("\nBFS Traversal Step-by-Step:")

    step = 1
    while queue:
        print(f"\nStep {step}:")
        print("Queue:", list(queue))
        
        node = queue.popleft()
        if node not in visited:
            print("Visiting:", node)
            
        bfs_path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"Added {neighbor} to queue")

        step += 1

    return bfs_path

start_node = input("\nEnter starting node: ")

# Run BFS
bfs_result = bfs(graph, start_node)
print("\nFinal BFS Path:", bfs_result)
