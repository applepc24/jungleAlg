import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

answer = 0
dirs = [(1,0), (-1, 0), (0,-1), (0,1)]

def dfs(r, c, mask, length):
    global answer
    if length > answer:
        answer = length
    
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not(0 <= nr < R and 0<= nc < C):
            continue
        
        ch = grid[nr][nc]
        bit = ord(ch) - ord('A')

        if (mask & (1 << bit)) != 0:
            continue
        
        dfs(nr, nc, mask | (1 << bit), length + 1)

start_ch = grid[0][0]
start_bit = ord(start_ch) - ord("A")
start_mask = (1 << start_bit)
dfs(0, 0, start_mask, 1)
print(answer)