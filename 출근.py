import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

dist = [[-1] * C for _ in range(R)]
q = deque()

for c in range(C):
    if grid[0][c] == 1:
        dist[0][c] = 0
        q.append((0,c))

if R == 1 and q:
    print(0)
    sys.exit(0)

while q:
    r, c = q.popleft()
    d = dist[r][c]

    if r == R -1:
        print(d)
        break

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = d + 1
                q.append((nr, nc))
else:
    print(-1)