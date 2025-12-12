import sys
input = sys.stdin.readline
import heapq

M, N = map(int, input().split())
board = [input().strip() for _ in range(N)]
INF = 10 ** 9
dist = [[INF] * M for _ in range(N)]
hq = []
heapq.heappush(hq, (0, 0, 0))
dist[0][0] = 0
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while hq:
    broken, x, y = heapq.heappop(hq)

    if broken > dist[x][y]:
        continue
    
    if x == N-1 and y == M-1:
        print(broken)
        sys.exit(0)
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            nb = broken+(1 if board[nx][ny] == '1' else 0)
            if nb < dist[nx][ny]:
                dist[nx][ny] = nb
                heapq.heappush(hq, (nb, nx, ny))

print(dist[N-1][M-1])