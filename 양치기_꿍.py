import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
map = [list(input().strip()) for _ in range(R)]
vis = [[False] * C for _ in range(R)]

ans_wolf = 0
ans_sheep = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(R):
    for j in range(C):
        if map[i][j] == '#' or vis[i][j]:
            continue
        
        q = deque([(i, j)])
        vis[i][j] = True
        sheep = 0
        wolf = 0
        
        while q:
            x, y = q.popleft()
            if map[x][y] == 'k':
                sheep += 1
            elif map[x][y] == 'v':
                wolf += 1
            
            for dx, dy in dirs:
                nx, ny = x + dx , y + dy
                if 0 <= nx < R and 0<= ny < C and not vis[nx][ny] and map[nx][ny] != '#':
                    vis[nx][ny] = True
                    q.append((nx, ny))
        
        if sheep > wolf:
            ans_sheep += sheep
        else:
            ans_wolf += wolf
    
print(ans_sheep, ans_wolf)