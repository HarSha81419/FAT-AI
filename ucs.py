import heapq

nodes = input("Enter the nodes (space separated): ").split()

graph = {node : [] for node in nodes}

e = int(input("Enter the number of edges: "))
edges = []

for _ in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    graph[u].append((v, cost))

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        print(f"Visiting {node}, Cost so far: {cost}")

        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = ucs(graph, start, goal)

print("\n✅ Goal Found!")
print("Path:", path)
print("Total Cost:", cost)