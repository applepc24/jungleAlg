import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

grid = [list(input().strip()) for _ in range(N)]
dirs = [(1,0), (-1,0), (0,1), (0, -1)]

def bfs(sx, sy, visited, blind):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    color = grid[sx][sy]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if not blind:
                        if grid[nx][ny] == color:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                    else:
                        if color == 'B':
                            if grid[nx][ny] == color:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                        else:
                            if grid[nx][ny] == 'G' or grid[nx][ny] == 'R':
                                visited[nx][ny] = True
                                q.append((nx,ny))

normal = 0
blind = 0

visited_n = [[False] * N for _ in range(N)]
visited_g = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited_n[i][j]:
            bfs(i, j, visited_n, False)
            normal += 1
        if not visited_g[i][j]:
            bfs(i, j, visited_g, True)
            blind += 1

print(normal, blind)
            