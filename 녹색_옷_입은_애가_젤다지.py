import sys
import heapq

input = sys.stdin.readline
INF = 10**9

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
tc = 1

while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    pq = []
    dist[0][0] = grid[0][0]
    heapq.heappush(pq, (dist[0][0], 0, 0))

    while pq:
        cost, x, y = heapq.heappop(pq)

        if cost > dist[x][y]:
            continue

        if x == n-1 and y == n-1:
            break

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                ncost = cost + grid[nx][ny]
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(pq, (ncost,nx,ny))

    print(f"Problem {tc}: {dist[n-1][n-1]}")
    tc += 1 