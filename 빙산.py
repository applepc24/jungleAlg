import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def count_ice():
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque([(i,j)])
                visited[i][j] = True
            
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx,  ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    return cnt

def melt():
    melt_amount = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                sea = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] == 0:
                            sea += 1
                melt_amount[i][j] = sea

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                board[i][j] = max(0, board[i][j] - melt_amount[i][j])

year = 0
while True:
    pieces = count_ice()

    if pieces >= 2:
        print(year)
        break

    if pieces == 0:
        print(0)
        break

    melt()
    year += 1