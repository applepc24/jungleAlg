import sys
input = sys.stdin.readline
from collections import deque

grid = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

pos = {}
for i in range(5):
    for j in range(5):
        if 1 <= grid[i][j] <= 6:
            pos[grid[i][j]] = (i, j)

dirs = ((1,0), (-1,0), (0,-1), (0,1))

def bfs(sr, sc, tr, tc):
    if (sr, sc) == (tr, tc):
        return 0
    dist = [[-1] * 5 for _ in range(5)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and grid[nr][nc] != -1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                if (nr, nc) == (tr, tc):
                    return dist[nr][nc]
                q.append((nr, nc))
    return -1

cur_r, cur_c = r, c
ans = 0
for i in range(1, 7):
    tr, tc = pos[i]
    d = bfs(cur_r, cur_c, tr, tc)
    if d == -1:
        print(-1)
        sys.exit(0)
    else:
        ans += d
        cur_r, cur_c = tr, tc

print(ans)
