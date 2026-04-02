import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

dist = [[-1] * M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j))
            dist[i][j] = 0

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dist[i][j])

print(ans)