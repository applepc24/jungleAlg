import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [i for i in range(101)]


for _ in range(n + m):
    s, e = map(int, input().split())
    grid[s] = e

q = deque()
q.append(1)
dist = [-1] * 101
dist[1] = 0

while q:
    x = q.popleft()
    for dice in range(1, 7):
        nx = x + dice
        if nx > 100:
            continue
        nx = grid[nx]

        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

print(dist[100])