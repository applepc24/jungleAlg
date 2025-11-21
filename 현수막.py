import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dirs = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (1,1),(-1,-1), (1, -1)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))

count = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            count += 1

print(count)