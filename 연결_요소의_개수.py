import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N , M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# for key in graph:
#     graph[key].sort()

def bfs(graph, start,visited):
    queue = deque([start])
    visited.add(start)
    
    while queue:
        v = queue.popleft()
        for nei in graph[v]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)


visited = set()
count = 0

for node in range(1 , N+1):
    if node not in visited:
        bfs(graph, node, visited)
        count +=1
print(count)
