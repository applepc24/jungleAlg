import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
for i in range(N):
    for j in range(N):
        max_h = max(max_h, board[i][j])

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(sx, sy, rain, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
        
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] > rain:
                    visited[nx][ny] = True
                    q.append((nx, ny))

answer = 0

for rain in range(max_h):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > rain and not visited[i][j]:
                bfs(i, j, rain, visited)
                count += 1
    answer = max(answer, count)

print(answer)