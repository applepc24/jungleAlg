import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
sizes = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            cnt = 1

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cnt += 1
            sizes.append(cnt)

sizes.sort()
print(len(sizes))
for s in sizes:
    print(s)   
