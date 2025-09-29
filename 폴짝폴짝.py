import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

dist = [-1] * (N + 1)
dist[a] = 0

q = deque([a])

while q:
    p = q.popleft()
    if p == b:
        break
    s = A[p]
    nxt = p + s
    while nxt <= N:
        if dist[nxt] == -1:
            dist[nxt] = dist[p] + 1
            q.append(nxt)
        nxt += s
    
    nxt = p - s
    while nxt >= 1:
        if dist[nxt] == -1:
            dist[nxt] = dist[p] + 1
            q.append(nxt)
        nxt -= s
print(dist[b])
