import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
dirs = [(2,1), (-2,1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    
    if sx == fx and sy == fy:
        print(0)
        continue
    
    dist = [[-1] * N for _ in range(N)]
    q= deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    while q:
        x, y  = q.popleft()
        if x == fx and y == fy:
            print(dist[x][y])
            break
        
        for dx, dy in dirs:
            nx, ny  = x + dx, y +dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))



