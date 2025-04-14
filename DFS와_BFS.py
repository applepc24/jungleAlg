N, M, start = map(int, input().split())

from collections import defaultdict, deque
graph = defaultdict(list)

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

def dfs(graph, v, visited):
    visited.add(v)
    print(v, end = ' ')
    for nei in graph[v]:
        if nei not in visited:
            dfs(graph, nei, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for nei in graph[v]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

dfs(graph, start, set())
print()
bfs(graph, start)


        
