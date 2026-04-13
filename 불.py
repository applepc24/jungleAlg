import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

fire_dist = [[-1] * C for _ in range(R)]
jihun_dist = [[-1] * C for _ in range(R)]

fire_q = deque()
jihun_q = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            fire_q.append((i,j))
            fire_dist[i][j] = 0
        if board[i][j] == 'J':
            jihun_q.append((i,j))
            jihun_dist[i][j] = 0

while fire_q:
    x, y = fire_q.popleft()
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] != '#' and fire_dist[nx][ny] == -1:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                fire_q.append((nx, ny))

while jihun_q:
    x, y = jihun_q.popleft()

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        next_time = jihun_dist[x][y] + 1

        if not (0 <= nx < R and 0 <= ny < C):
            print(next_time)
            sys.exit(0)
        
        if board[nx][ny] == '#':
            continue

        if jihun_dist[nx][ny] != -1:
            continue

        if fire_dist[nx][ny] != -1 and fire_dist[nx][ny] <= next_time:
            continue

        jihun_dist[nx][ny] = next_time
        jihun_q.append((nx, ny))
print('IMPOSSIBLE')