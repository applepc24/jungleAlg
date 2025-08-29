import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for nei in graph[v]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count =0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)

