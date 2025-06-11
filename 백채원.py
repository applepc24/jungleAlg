import sys
import heapq

input = sys.stdin.readline
INF = int(1e18)

def djikstra(starts):
    dist = [INF] * (N+1)
    pq = []
    for s in starts:
        dist[s] = 0
        heapq.heappush(pq, (0,s))
    while pq:
        d, now = heapq.heappop(pq)
        if d > dist[now]:
            continue
        for nxt, cost in graph[now]:
            if dist[nxt] > d + cost:
                dist[nxt] = d +cost
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist
            

N, M, K = map(int, input().split())

graph= [[]for _ in range(N+1)]

for _ in range(M):
    a,b,cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

followers = list(map(int, input().split()))

dist_won = djikstra([1])
dist_foll = djikstra(followers)

result = []
for i in range(2, N+1):
    if dist_won[i] < dist_foll[i]:
        result.append(i)

if result:
    print(*result)
else:
    print(0)