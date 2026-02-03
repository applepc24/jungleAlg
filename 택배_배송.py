import sys
import heapq

input = sys.stdin.readline
INF = 10**18

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append((b,c))
    node[b].append((a,c))

dist = [INF] * (n+1)
dist[1] = 0

pq = [(0,1)]

while pq:
    cost, u = heapq.heappop(pq)

    if cost > dist[u]:
        continue

    if u == n:
        print(dist[n])
        break

    for v, w in node[u]:
        ncost = cost + w
        if ncost < dist[v]:
            dist[v] = ncost
            heapq.heappush(pq, (ncost, v))