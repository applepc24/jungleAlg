import sys
input= sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

vis = [[False] * M for _ in range(N)]
dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]

def bfs(sr, sc):
    ch = grid[sr][sc]
    q = deque([(sr, sc)])
    vis[sr][sc] = True
    cnt = 0
    minr = maxr = sr
    minc = maxc = sc

    while q:
        r, c = q.popleft()
        cnt += 1
        minr = min(minr, r)
        maxr = max(maxr, r)
        minc = min(minc, c)
        maxc = max(maxc, c)

        for dr, dc in dirs:
            nr, nc = r + dr, c +dc
            if 0 <= nr < N and 0 <= nc < M and not vis[nr][nc] and grid[nr][nc] == ch:
                vis[nr][nc] = True
                q.append((nr, nc))
        
    area = (maxr - minr +1) * (maxc - minc + 1)
    return area == cnt

pretty = True
for i in range(N):
    for j in range(M):
        if not vis[i][j]:
            if not bfs(i, j):
                pretty = False
                break
    if not pretty:
        break
print("dd" if pretty else "BaboBabo")