import random

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]

def total_dist(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += dist[route[i]][route[i+1]]
    cost += dist[route[-1]][route[0]]
    return cost

def get_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    
    print(neighbors)
    return neighbors

def hill_climbing():
    current = cities[:]
    random.shuffle(current)

    print("Initial Route: ", current, "Cost: ", total_dist(current))

    while True:
        neighbors = get_neighbors(current)
        next_route = min(neighbors, key = total_dist)

        print("Best Neighbor: ", next_route, "Cost: ", total_dist(next_route))

        if total_dist(next_route) >= total_dist(current):
            print("Reached local Optimum")
            return current
        
        current = next_route

result = hill_climbing()
print("Final Route: ", result)