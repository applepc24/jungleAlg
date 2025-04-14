import sys
import heapq
input = sys.stdin.readline

n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

heap = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    current = heapq.heappop(heap)
    result.append(current)

    for nei in graph[current]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            heapq.heappush(heap, nei)

print(*result)



    # queue가 빌때까지
    while queue:
        # 우선 순위 큐에서 현재 가장 비용이 적은 노드를 꺼냄
        # dist는 지금까지의 누적 비용, now는 현재 노드
        dist, now = heapq.heappop(queue)
        # 이미 더 짧은 거리로 방문한 적이 있다면 이번 경로는 무시
        if dist > distance[now]:
            continue

        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))