import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

R, C, T = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

start_r = start_c = None
sweet_id = {}
sweet_count = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'G':
            start_r, start_c = r,c
        elif grid[r][c] == 'S':
            sweet_id[(r, c)] = sweet_count
            sweet_count += 1

dirs = [(-1,0), (1,0), (0,-1), (0,1),(0,0)]


def dfs(r, c, t_left, mask):
    gain = 0
    new_mask = mask

    if (r, c) in sweet_id:
        sid = sweet_id[(r, c)]
        if (mask & (1 << sid)) == 0:
            gain = 1
            new_mask = mask | (1 << sid)
    
    if t_left == 0:
        return gain
    
    best_next = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c +dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            cand = dfs(nr, nc, t_left -1, new_mask)
            if cand > best_next:
                best_next = cand
    return gain + best_next
answer = dfs(start_r, start_c, T , 0)
print(answer)