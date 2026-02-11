import sys
from collections import deque

input = sys.stdin.readline

n, L, R = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1,0), (-1,0), (0,1), (0, -1)]

days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            q = deque([(i, j)])
            visited[i][j] = True
            union = [(i, j)]
            total = grid[i][j]

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y +dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        diff = abs(grid[x][y] - grid[nx][ny])
                        if L <= diff <= R:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            union.append((nx, ny))
                            total += grid[nx][ny]
            
            if len(union) >= 2:
                new_pop = total // len(union)
                for x, y in union:
                    if grid[x][y] != new_pop:
                        moved = True
                    grid[x][y] = new_pop
    
    if not moved:
        break
    days += 1

print(days)