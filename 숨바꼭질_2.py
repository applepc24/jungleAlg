import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100001
dist = [-1] * MAX
count = [0] * MAX

q = deque([N])
dist[N] = 0
count[N] = 1

while q:
    cur = q.popleft()

    for nxt in (cur-1, cur+1, cur * 2):
        if 0 <= nxt < MAX:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                count[nxt] = count[cur]
                q.append(nxt)
            elif dist[nxt] == dist[cur] + 1:
                count[nxt] += count[cur]

print(dist[K])
print(count[K])