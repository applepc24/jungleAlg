import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [[0] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]
dirs = [(1,0), (0,1), (-1,0), (0,-1)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

def bfs(sr, sc) -> int:
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 1 <= nr <= N and 1 <= nc <= M:
                if board[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cnt += 1
                    
    return cnt

answer = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i,j)
            answer = max(answer, cnt)

print(answer)