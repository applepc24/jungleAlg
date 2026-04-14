import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

rev_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())

    graph[a].append((b,t))
    rev_graph[b].append((a,t))

def dijk(start, g):
    INF = 10**9
    dist = [INF] * (N+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, now = heapq.heappop(pq)

        if cur_dist > dist[now]:
            continue

        for nxt, cost in g[now]:
            new_dist = cur_dist + cost

            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    
    return dist

dist_from_X = dijk(X, graph)
dist_to_X = dijk(X, rev_graph)

answer = 0

for i in range(1, N+1):
    total = dist_from_X[i] + dist_to_X[i]

    if total > answer:
        answer = total

print(answer)

