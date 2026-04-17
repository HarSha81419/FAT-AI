A STAR

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


ALPHA BETA

def alphabeta(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]
    
    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruned at MAX node (depth: {depth})")
                break

        return best
    
    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruned at MIN node (depth: {depth})")
                break
                
        return best

depth = int(input("Enter the max depth: "))
n = 2 ** depth

print(f"Enter {n} node values: ")
values = list(map(int, input().split()))

is_max = depth % 2 != 0

result = alphabeta(0, 0, is_max, values, float('-inf'), float('inf'), depth)

print("Optimal Value: ", result)

AND OR GRAPH


BAYESIAN

# -------- PROBABILITIES --------

P_R = 0.2  # P(R=True)
P_not_R = 1 - P_R

# P(S=True | R)
P_S_given_R = 0.01
P_S_given_not_R = 0.4

# P(W=True | S, R)
def P_W_given_S_R(S, R):
    if S and R:
        return 0.99
    if S and not R:
        return 0.90
    if not S and R:
        return 0.80
    return 0.00


# -------- CALCULATE P(W) --------
def compute_P_W():
    total = 0

    for R in [True, False]:
        for S in [True, False]:

            # P(R)
            p_r = P_R if R else P_not_R

            # P(S | R)
            if R:
                p_s = P_S_given_R if S else (1 - P_S_given_R)
            else:
                p_s = P_S_given_not_R if S else (1 - P_S_given_not_R)

            # P(W | S, R)
            p_w = P_W_given_S_R(S, R)

            total += p_r * p_s * p_w

    return total


# -------- CALCULATE P(R AND W) --------
def compute_P_R_and_W():
    total = 0

    R = True  # Fix R = True

    for S in [True, False]:

        p_r = P_R

        # P(S | R=True)
        p_s = P_S_given_R if S else (1 - P_S_given_R)

        # P(W | S, R)
        p_w = P_W_given_S_R(S, R)

        total += p_r * p_s * p_w

    return total


# -------- BAYES RULE --------
P_W = compute_P_W()
P_R_and_W = compute_P_R_and_W()

P_R_given_W = P_R_and_W / P_W

print("P(WetGrass=True) =", P_W)
print("P(Rain=True AND WetGrass=True) =", P_R_and_W)
print("P(Rain=True | WetGrass=True) =", P_R_given_W)

BFS

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


DFS

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

DLS

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

GBFS

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

HILL CLIMBING

import ast

def hill(g, h, s):
    cur = s
    path = [cur]
    visited = set()
    while True:
        visited.add(cur)
        neighbors = [x for x in g.get(cur, []) if x not in visited]
        nxt = max(neighbors, key=lambda x: h[x], default=None)
        if not nxt or h[nxt] <= h[cur]:
            return cur, path
        cur = nxt
        path.append(cur)

g = ast.literal_eval(input("Enter graph dictionary: "))
h = ast.literal_eval(input("Enter heights dictionary: "))
s = ast.literal_eval(input("Enter start node: "))  # Fixed
peak, path = hill(g, h, s)
print("Hill Climbing path:", " -> ".join(str(n) for n in path))
print(f"Peak reached: {peak} with value {h[peak]}")

IDDFS

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

M_C

from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    
    if(m > 0 and c > m):
        return False
    
    m_right = 3 - m
    c_right = 3 - c

    if(m_right > 0 and c_right > m_right):
        return False
    
    return True

def bfs():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        print("Visiting: ", (m, c, boat))

        if(m, c, boat) == goal:
            return path + [(m, c, boat)]
        
        if(m, c, boat) in visited:
            continue

        visited.add((m, c, boat))

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)
            
            if is_valid(*new_state[:2]):
                queue.append((new_state, path + [(m, c, boat)]))

    return None

solution = bfs()

if solution:
    print("Solution Found: ")
    for step in solution:
        print(step)
else:
    print("No Solution")

MINIMAX

def minimax(values, depth, is_max):
    if depth == 0:
        return values[0]
    
    new_values = []

    for i in range(0, len(values), 2):
        if is_max:
            new_values.append(max(values[i], values[i+1]))
        else:
            new_values.append(min(values[i], values[i+1]))
    
    return minimax(new_values, depth - 1, not is_max)
        
depth = int(input("Enter the maxmium depth: "))
n = 2 ** depth

print(f"Enter {n} leaf values: ")
values = list(map(int, input().split()))

if depth % 2 == 0:
    is_max = False
else:
    is_max = True

result = minimax(values, depth, is_max)

print("Optimal Value: ", result)

MONKEYBANANA

def and_or_search(state, goal):
    print("Current State: ", state)

    if state["has_banana"]:
        print("Goal Reached!")
        return True

    if state["monkey_pos"] != state["box_pos"]:
        print("OR: Move monkey to Box")
        new_state = state.copy()
        new_state["monkey_pos"] = new_state["box_pos"]
        return and_or_search(new_state, goal)
    
    print("AND: Performing sequence actions")

    if state["box_pos"] != state["banana_pos"]:
        print("-> push box to banana")
        state["box_pos"] = state["banana_pos"]
        state["monkey_pos"] = state["banana_pos"]

    if not state["on_box"]:
        print("-> Climb the Box")
        state["on_box"] = True
    
    if state["on_box"] and state["monkey_pos"] == state["banana_pos"]:
        print("-> Grab Banana")
        state["has_banana"] = True

    return and_or_search(state, goal)

state = {
    "monkey_pos" : "A",
    "box_pos" : "B",
    "banana_pos" : "C",
    "on_box" : False,
    "has_banana" : False
}

goal = True

result = and_or_search(state, goal)

if result:
    print("Monkey got the banana!")
else:
    print("Failed")

N QUEENS

N = int(input("Enter number of queens: "))
board = [[0]*N for _ in range(N)]

def safe(r, c):
    for i in range(c):
        if board[r][i] == 1:
            return False
    
    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i, j = r, c

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True

def solve(c):
    if c >= N:
        return True
    
    for i in range(N):
        if safe(i, c):
            board[i][c] = 1
            if solve(c + 1):
                return True
            board[i][c] = 0
    return False

solve(0)
print("Solution: ")
for row in board:
    print(row)

TIC TAC TOE

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

win_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    for combo in win_combos:
        # check each position one by one
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def is_board_full():
    for spot in board:
        if spot == ' ':
            return False
    return True

def get_empty_spots():
    empty = []
    for i in range(9):
        if board[i] == ' ':
            empty.append(i)
    return empty

# ---------- MINIMAX (SIMPLE VERSION) ----------

def minimax(is_ai_turn):
    # --- Base cases ---
    if check_winner('O'):   # AI won
        return 1
    if check_winner('X'):   # Player won
        return -1
    if is_board_full():     # Draw
        return 0

    if is_ai_turn:
        best_score = -100
        for spot in get_empty_spots():
            board[spot] = 'O'                    # try this move
            score = minimax(False)               # see what happens next
            board[spot] = ' '                    # undo the move
            if score > best_score:               # keep the best score
                best_score = score
        return best_score
    else:
        best_score = 100
        for spot in get_empty_spots():
            board[spot] = 'X'                    # try this move
            score = minimax(True)                # see what happens next
            board[spot] = ' '                    # undo the move
            if score < best_score:               # keep the worst score
                best_score = score
        return best_score

def ai_move():
    best_score = -100
    best_move = -1

    for spot in get_empty_spots():
        board[spot] = 'O'                        # try this move
        score = minimax(False)                   # get score for this move
        board[spot] = ' '                        # undo the move
        if score > best_score:                   # found a better move
            best_score = score
            best_move = spot

    board[best_move] = 'O'
    print(f"AI plays position {best_move + 1}")

# ---------- GAME LOOP ----------

def play_game():
    print("TIC TAC TOE - You(X) vs AI(O)")
    print("Positions: 1-9")

    while True:
        print_board()

        # Player turn
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
            except ValueError:
                print("Enter a number!")
                continue
            if move < 0 or move > 8:
                print("Enter 1-9!")
                continue
            if board[move] != ' ':
                print("Spot taken!")
                continue
            break

        board[move] = 'X'

        if check_winner('X'):
            print_board()
            print("You win!")
            break
        if is_board_full():
            print_board()
            print("Draw!")
            break

        # AI turn
        ai_move()

        if check_winner('O'):
            print_board()
            print("AI wins!")
            break
        if is_board_full():
            print_board()
            print("Draw!")
            break

play_game()

TLS

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

UCS

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

WATERJUG

import heapq

cap1 = int(input("Enter the cap of J1: "))
cap2 = int(input("Enter the cap of J2: "))
target = int(input("Enter the target: "))

def waterJug():
    visited = set()
    pq = [(0, (0, 0))]

    while pq:
        cost, (x, y) = heapq.heappop(pq)
        print("Visiting: ", (x, y))

        if x == target or y == target:
            print("Goal state: ", (x, y))
            return
        
        if (x, y) in visited:
            continue
        visited.add(x, y)

        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in next_states:
            if state not in visited:
                heapq.heappush(pq, (cost + 1, state))

waterJug()

WUMPUS

# Simple Wumpus World (4x4 grid)

grid = [
    ["", "P", "", ""],
    ["", "W", "", "P"],
    ["", "", "", ""],
    ["G", "", "", ""]
]

# Start position
x, y = 0, 0

def move(direction):
    global x, y

    if direction == "right":
        y += 1
    elif direction == "left":
        y -= 1
    elif direction == "up":
        x -= 1
    elif direction == "down":
        x += 1

    check_position()


def check_position():
    global x, y

    # Check boundaries
    if x < 0 or y < 0 or x > 3 or y > 3:
        print("Out of bounds!")
        return

    cell = grid[x][y]

    if cell == "P":
        print("Fell into Pit! Game Over ❌")
    elif cell == "W":
        print("Eaten by Wumpus! Game Over ❌")
    elif cell == "G":
        print("You found Gold! You Win 💰")
    else:
        print("Safe move 👍")


# Demo moves
move("right")
move("right")
move("down")
move("down")
move("down")
