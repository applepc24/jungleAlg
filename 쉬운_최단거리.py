import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
sx = sy = -1

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if row[j] == 2:
            sx, sy = i, j

dist = [[-1] * m for _ in range(n)]
dist[sx][sy] = 0

q = deque()
q.append((sx, sy))

dirs = [(1,0), (-1,0), (0, 1), (0, -1)]

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] != 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end= " ")
        else:
            print(dist[i][j], end = " ")
    print()

