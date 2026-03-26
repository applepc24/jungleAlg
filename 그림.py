import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[False] * M for _ in range(N)]


pic_cnt = 0
max_area = 0

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    area = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
        
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    area += 1
                    q.append((nx, ny))
    return area

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            area = bfs(i, j)
            pic_cnt += 1
            max_area = max(area, max_area)

print(pic_cnt)
print(max_area)
