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