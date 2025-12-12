import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

INF = 10**9
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    out = []
    for j in range(1, n+1):
        if dist[i][j] == INF:
            out.append(0)
        else:
            out.append(dist[i][j])
    print(*out)