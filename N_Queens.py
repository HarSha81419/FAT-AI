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