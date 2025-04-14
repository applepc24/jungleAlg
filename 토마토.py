import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())
tomato = []
for _ in range(h):
    tomato_floor = [list(map(int, input().split())) for _ in range(n)]
    tomato.append(tomato_floor)

dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

queue = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                queue.append((z, x, y))

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz, nx, ny))
            
result = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                print(-1)
                exit()
            result = max(result, tomato[z][x][y])
print(result -1)