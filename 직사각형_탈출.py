import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[0] * (M+1)]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    g.append(row)

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

S = [[0] * (M + 1) for _ in range(N+1)]
for r in range(1, N+1):
    acc = 0
    for c in range(1, M + 1):
        acc += g[r][c]
        S[r][c] = S[r-1][c] + acc

def can_place(r, c):
    r2, c2 = r + H - 1, c + W - 1
    if r < 1 or c < 1 or r2 > N or c2 > M:
        return False
    total = S[r2][c2] - S[r-1][c2] - S[r2][c-1] + S[r-1][c-1]
    return total == 0

RMAX, CMAX = N - H + 1, M - W + 1
dist = [[-1] * (M+1) for _ in range(N+1)]

dirs = [(1,0), (-1,0), (0,-1), (0,1)]

q = deque()
q.append((Sr, Sc))
dist[Sr][Sc] = 0

while q:
    r, c = q.popleft()
    if (r, c) == (Fr, Fc):
        print(dist[r][c])
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 1 <= nr <= RMAX and 1 <= nc <= CMAX:
            if dist[nr][nc] == -1 and can_place(nr, nc):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
else:
    print(-1)

