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