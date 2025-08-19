import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cnt = [0] * N
visit = [False] * N
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v_ = map(int, input().split())
    graph[u].append(v_)
    graph[v_].append(u)
    cnt[u] += 1
    cnt[v_] += 1

q = deque()

for i in range(N):
    if cnt[i] == 1:
        q.append(i)
        visit[i] = True

while True:
    size = len(q)
    if size <= 2:
        break

    for _ in range(size):
        node = q.popleft()
        cnt[node] -= 1
        for neighbor in graph[node]:
            if not visit[neighbor]:
                cnt[neighbor] -= 1
                if cnt[neighbor] == 1:
                    visit[neighbor] = True
                    q.append(neighbor)

result = [i for i in range(N) if cnt[i] > 0]
print(*sorted(result))
