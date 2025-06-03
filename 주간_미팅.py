import heapq

N, V, E = map(int, input().split())
a, b = map(int, input().split())
homes = list(map(int, input().split()))

#그래프 양방향을 만들기
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

#다익스트라 함수 만들기

def dijkstra(start):
    INF = int(1e9)
    distance = [[INF] * (V+1)]
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for neighbor, cost in graph[now]:
            if distance[neighbor] > dist + cost:
                distance[neighbor] = dist + cost
                heapq.heappush(pq, (distance[neighbor], neighbor))
    return distance

dist_from_a = dijkstra(a)
dist_from_b = dijkstra(b)

total = 0
for home in homes:
    total += dist_from_a[home] + dist_from_b[home]

print(total)