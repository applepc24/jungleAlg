import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)
visited = [False] * (MAX + 1)

q = deque()
q.append(n)
visited[n] = True

while q:
    x = q.popleft()
    
    if x == k:
        print(dist[x])
        break
    
    for nx in (x+1, x-1, x*2):
        if 0 <= nx <= MAX and not visited[nx]:
            dist[nx] = dist[x] + 1
            visited[nx] = True
            q.append(nx)