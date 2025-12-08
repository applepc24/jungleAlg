import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
INF = 10**9
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

dist = [INF] * (V+1)
dist[K] = 0

hq = []
heapq.heappush(hq, (0, K))

while hq:
    d, now = heapq.heappop(hq)

    if d > dist[now]:
        continue
    
    for nxt, w in graph[now]:
        nd = d + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(hq, (nd, nxt))

for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
    