import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

land = [list(input().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

W_cnt = 0
B_cnt = 0

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sy][sx] = True
    color = land[sy][sx]
    cnt = 1
    while q:
        sx, sy = q.popleft()

        for dx, dy in dirs:
            nx, ny  = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if land[ny][nx] == color and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    cnt += 1
    return color, cnt

for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            color, cnt = bfs(x, y)
        
            if color == 'W':
                W_cnt += cnt * cnt
            else:
                color == "B"
                B_cnt += cnt * cnt

print(W_cnt, B_cnt)