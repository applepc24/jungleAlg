import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

def bfs(sx, sy):
    q = deque([(sx,sy)])
    visited[sy][sx] = True
    area = 1

    while q:
        x, y = q.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    area += 1
                    visited[ny][nx] = True
                    q.append((nx, ny))
    return area

total_cnt = 0
cnt = []
visited = [[False] * N for _ in range(M)]

for y in range(M):
    for x in range(N):
        if board[y][x] == 0 and not visited[y][x]:
            cnt.append(bfs(x,y))
            total_cnt += 1

cnt.sort()
print(total_cnt)
print(*cnt)