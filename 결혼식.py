from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0

q = deque([1])

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

answer = 0
for person in range(2, n+1):
    if 1 <= dist[person] <= 2:
        answer += 1
print(answer)