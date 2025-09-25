import sys
import heapq
from collections import deque
input = sys.stdin.readline

INF = 10**9
N,M,X,Y = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

B = list(map(int, input().split()))

security_time = [INF] * N
q = deque()

for b in B:
    security_time[b-1] = 1
    q.append(b-1)
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if security_time[nxt] == INF:
            security_time[nxt] = security_time[cur] + 2
            q.append(nxt)
for i in range(N):
    if security_time[i] == INF and A[i] > 0:
        print(-1)
        sys.exit(0)

profits = []
for i in range(N):
    T = security_time[i]
    # 보안 시각 T 보다 작은 {2,4,6,...} 의 개수 = (T-1)//2
    earn_times = 0 if T == INF else (T - 1) // 2
    if earn_times > 0:
        profits.append(A[i] * earn_times)


profits.sort(reverse = True)
answer = sum(profits[:X])
print(answer)