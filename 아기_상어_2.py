from collections import deque

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

direct = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)]

queue = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            queue.append((i, j))

distance = [[-1] * m for _ in range(n)]
for x, y in queue:
    distance[x][y] = 0

while queue:
    x, y = queue.popleft()
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0<= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] +1
            queue.append((nx, ny))

max_dist = max(map(max, distance))
print(max_dist)

