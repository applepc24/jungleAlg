import sys
from collections import deque

n, k = map(int, input().split())
child = [[] for _ in range(n)]
for _ in range(n - 1):
    c, v = map(int, input().split())
    child[c].append(v)

values = list(map(int, input().split()))

node_k = -1
for i, v in enumerate(values):
    if v == k:
        node_k = i
        break
    
depth = [-1] * n
q = deque([0])
depth[0] = 0
while q:
    u = q.popleft()
    for w in child[u]:
        depth[w] = depth[u] + 1
        q.append(w)

print(depth[node_k])
