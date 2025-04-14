import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
# 경로와 가중치가 들어가는 빈 배열을 만든다.
graph = [[] for _ in range(n+1)]

# m개의 경로들을 돌면서 빈배열에 경로와 가중치를 집어 넣는다.
for _ in range(m):
    u,v,cost = map(int, input().split())
    graph[u].append((v, cost))

print(graph)
# 주어진 시작점과 끝점을 받는다.
start, end = map(int, input().split())
# 아무것도 모른다의 의미로 사실상 무한대처럼 쓰는 숫자
INF = int(1e9)
# 각 경로마다의 가중치를 넣고 비교하는 배열을 만든다 (INF로 채움)
distance = [INF] * (n+1)

def dijkstra(start):
    # 경로의 가중치를 비교할 빈 배열을 만든다.
    queue = []
    # queue배열안에 초기값을 넣어준다
    heapq.heappush(queue, (0, start))
    # 첫 가중치는 0
    distance[start] = 0

    while queue:
        dist , now = heapq.heappop(queue)

        if dist > distance[now]:
            continue:
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))


dijkstra(start)
print(distance[end])