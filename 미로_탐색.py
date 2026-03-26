import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

q = deque([(0,0)])

while q:
    x, y = q.popleft()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

print(board[N-1][M-1])