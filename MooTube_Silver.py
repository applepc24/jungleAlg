import sys
from collections import deque
input = sys.stdin.readline

N,Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(k, start):
    visited = [False] * (N+1)
    dq = deque([start])
    visited[start] = True
    count = 0

    while dq:
        cur = dq.popleft()
        for nxt, w in graph[cur]:
            if not visited[nxt] and w >= k:
                visited[nxt] = True
                dq.append(nxt)
                count += 1
    return count

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k,v))