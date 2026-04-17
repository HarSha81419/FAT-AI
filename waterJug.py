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