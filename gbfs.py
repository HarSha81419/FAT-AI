import heapq

nodes = input("Enter the nodes (space separated): ").split()

graph = {node : [] for node in nodes}

e = int(input("Enter the number of edges: "))
edges = []

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

heuristic = {}
print("Enter heuristic values (in format node value): ")

for _ in range(len(nodes)):
    node, h = input().split()
    heuristic[node] = int(h)

def gbfs(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
        
    return None

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path = gbfs(graph, start, goal, heuristic)

if path:
    print("\n✅ Goal Found!")
    print("Path Found:", path)
else:
    print("\n❌ Goal not reachable")