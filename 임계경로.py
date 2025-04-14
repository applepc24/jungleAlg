import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
time = [0] * (n + 1)

# 그래프 입력 받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    reverse_graph[b].append((a, cost))
    in_degree[b] += 1

start, end = map(int, input().split())

# 위상 정렬로 최장 경로 구하기
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for next_node, cost in graph[now]:
        if time[next_node] < time[now] + cost:
            time[next_node] = time[now] + cost
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

# 역추적 BFS로 경로 간선 개수 세기
count = 0
visited = [False] * (n + 1)
queue = deque([end])
visited[end] = True

while queue:
    now = queue.popleft()
    for prev, cost in reverse_graph[now]:
        if time[prev] + cost == time[now]:
            count += 1
            if not visited[prev]:
                visited[prev] = True
                queue.append(prev)

print(time[end])
print(count)