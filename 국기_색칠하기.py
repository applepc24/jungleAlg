import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]
B = [list(input().strip()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    color = A[sr][sc]
    cells = [(sr, sc)]
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and A[nr][nc] == color:
                visited[nr][nc] = True
                q.append((nr, nc))
                cells.append((nr, nc))
    return cells

def check():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                comp = bfs(i, j)
                s = set()
                for r, c in comp:
                    s.add(B[r][c])
                if len(s) != 1:
                    return False
    return True

print("YES" if check() else "NO")