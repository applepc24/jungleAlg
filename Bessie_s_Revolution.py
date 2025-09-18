import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

def open_road(r, c):
    return 0 <= r < N and 0<= c < N and grid[r][c] == '.'


dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

def nei(r, c):
    out = []
    for dr, dc in dirs:
        nr, nc = dr + r, dc + c
        if open_road(nr, nc):
            out.append((nr, nc))
    return out

def is_articultaion(r, c):
    nbrs = list(nei(r, c))
    if len(nbrs) < 2:
        return False
    
    a = nbrs[0]
    q = deque([a])
    vis = [[False] * N for _ in range(N)]
    vis[r][c] = True
    vis[a[0]][a[1]] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x +dx , y + dy
            if 0 <= nx < N and 0 <= ny < N and not vis[nx][ny] and grid[nx][ny] == '.':
                vis[nx][ny] = True
                q.append((nx, ny))
    
    for b in nbrs[1:]:
        if not vis[b[0]][b[1]]:
            return True
    return False

ans = 0
for r in range(N):
    for c in range(N):
        if grid[r][c] == '.':
            if is_articultaion(r, c):
                ans += 1
print(ans)

    
    