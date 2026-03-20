import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1] * (n+1)
q = deque([start])
visited[start] = 0

while q:
    cur = q.popleft()
    if cur == end:
        print(visited[cur])
        break

    for nxt in graph[cur]:
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
else:
    print(-1)