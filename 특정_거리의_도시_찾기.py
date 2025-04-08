import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)

def bfs(graph, start , K):
    N = len(graph) -1
    distance = [-1] * (N+1)
    distance[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()
        for nei in graph[current]:
            if distance[nei] == -1:
                distance[nei] = distance[current] + 1
                queue.append(nei)
    return [i for i in range(1, N+1) if distance[i] == K]


result = bfs(graph, X, K)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)

