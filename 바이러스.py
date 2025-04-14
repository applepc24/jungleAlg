cpuN = int(input())
M = int(input())

from collections import defaultdict, deque

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        v = queue.popleft()
        for nei in graph[v]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return len(visited) -1

print(bfs(graph, 1))