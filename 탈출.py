import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int, input().split())
maze = [list(map(str, input().strip())) for _ in range(R)]

water_time = [[-1] * C for _ in range(R)]
bibber_time = [[-1] * C for _ in range(R)]

water_q = deque()
bibber_q = deque()

for i in range(R):
    for j in  range(C):
        if maze[i][j] == '*':
            water_q.append((i,j))
            water_time[i][j] = 0
        if maze[i][j] == 'S':
            bibber_q.append((i,j))
            bibber_time[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while water_q:
    x,y = water_q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0 <= ny < C:
            if maze[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                water_q.append((nx,ny))

escaped = False
while bibber_q:
    x,y = bibber_q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] == 'D':
                print(bibber_time[x][y] + 1)
                escaped = True
                break
            if maze[nx][ny] == '.' and bibber_time[nx][ny] == -1:
                next_time = bibber_time[x][y] + 1
                if water_time[x][y] == -1 or next_time < water_time[nx][ny]:
                    bibber_time[nx][ny] = next_time
                    bibber_q.append((nx, ny))
    if escaped:
        break
if not escaped:
    print("KAKTUS")
        


        
