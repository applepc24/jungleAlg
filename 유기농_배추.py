import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dirs = [(1,0), (-1,0), (0,1), (0, -1)]

def bfs(sx, sy, land, visited, N, M):
    q = deque([(sx, sy)])
    visited[sy][sx] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if land[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))



for _ in range(T):
    M, N, K = map(int, input().split())
    land = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1
    count = 0

    for y in range(N):
        for x in range(M):
            if land[y][x] == 1 and not visited[y][x]:
                bfs(x, y,land, visited, N, M)
                count += 1
    
    print(count)