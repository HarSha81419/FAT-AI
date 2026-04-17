import heapq

nodes = input("Enter the nodes (space separated): ").split()

graph = {node : [] for node in nodes}

e = int(input("Enter the number of edges: "))

print("Enter the edges (in the format: u v cost): ")

for _ in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    graph[u].append((v, cost))

print("Enter the heuristic values (in the format: node value)")

heuristic = {}
for _ in range(len(nodes)):
    node, h = input().split()
    heuristic[node] = int(h)

def a_star(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        print(f"Visiting node {node}, g(n) = {g}, h(n) = {heuristic[node]}, f(n) = {f}")

        if node == goal:
            return path, g
        
        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node]:
                if neighbor not in visited:

                    new_g = cost + g
                    new_f = new_g + heuristic[neighbor]

                    heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return False, float('inf')

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path, cost = a_star(graph, start, goal, heuristic)

if path:
    print(f"Goal Found! Path: {path}, cost: {cost}")
else:
    print("Goal couldn't be reached!!!")