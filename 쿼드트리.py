import sys
input = sys.stdin.readline

N = int(input())

board = [input().strip() for _ in range(N)] 

def solve(r, c, size):
    first = board[r][c]
    same = True
    i = r
    while i < r + size and same:
        j = c
        row = board[i]
        while j < c + size:
            if row[j] != first:
                same = False
                break
            j += 1
        i += 1
    
    if same:
        return first
    
    half = size // 2
    ul = solve(r, c, half)
    ur = solve(r, c+ half, half)
    dl = solve(r+half, c, half)
    dr = solve(r + half, c+half, half)

    return '(' + ul + ur + dl + dr + ')'

print(solve(0, 0, N))
