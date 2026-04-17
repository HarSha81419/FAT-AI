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