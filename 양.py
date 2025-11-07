import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(input().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dirs = [(1,0), (-1,0), (0,1), (0, -1)]

total_sheep = 0
total_wolf = 0

def bfs(r,c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    wolf = 0
    sheep = 0
    if map[r][c] == 'o':
        sheep += 1
    elif map[r][c] == 'v':
        wolf += 1
    
    while q:
        sr, sc = q.popleft()
        for dr, dc in dirs:
            nr, nc = dr + sr, dc + sc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if map[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    if map[nr][nc] == 'o':
                        sheep += 1
                    elif map[nr][nc] == 'v':
                        wolf += 1
    return wolf, sheep

for i in range(N):
    for j in range(M):
        if not visited[i][j] and map[i][j] != "#":
            w, s = bfs(i,j)
            if s > w:
                total_sheep += s
            else:
                total_wolf += w

print(total_sheep, total_wolf)
