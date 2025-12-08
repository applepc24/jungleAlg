import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (N+1)
    dist[start] = 0

    q= deque()
    q.append(start)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    
    total = 0
    for i in range(1, N + 1):
        total += dist[i]
    return total

min =  10 ** 9
answer = -1

for i in range(1, N+1):
    s = bfs(i)
    if s < min:
        min = s
        answer = i
print(answer)