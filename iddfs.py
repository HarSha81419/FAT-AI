# -------- INPUT --------
nodes = input("Enter nodes (space separated): ").split()

graph = {}
for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges (format: u v):")

for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

def dls(graph, current, goal, depth, visited, path, level):
    print(f"Visiting {current}, Actual Depth: {level}")

    if current == goal:
        return True, level, path.copy()
    
    if depth == 0:
        return False, -1, []
    
    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            path.append(neighbor)
            found, result_depth, result_path = dls(graph, neighbor, goal, depth - 1, visited,path,  level + 1)
            if found:
                return True, result_depth, result_path
            
            path.pop()
    
    return False, -1, []

def iddfs(graph, start, goal):
    depth = 0

    while True:
        print(f"Trying Depth limit: {depth}")

        visited = set()
        path = [start]

        found, result_depth, result_path = dls(graph, start, goal, depth, visited, path, 0)

        if found:
            return result_depth, result_path
        
        depth+=1

start = input("Enter the Start node: ")
goal = input("Enter the Goal node: ")

depth_found, result_path = iddfs(graph, start, goal)

print("Goal Found!")
print("Depth of Goal: ", depth_found)
print("Path Found: ", result_path)