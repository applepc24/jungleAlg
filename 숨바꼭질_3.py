import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100000
INF = 10 ** 9

dist = [INF] * (MAX+1)
dist[n] = 0

pq = []
heapq.heappush(pq, (0, n))

while pq:
    time, x = heapq.heappop(pq)

    if time > dist[x]:
        continue
    
    if x == k:
        print(time)
        break
    
    nx = x * 2
    if 0 <= nx <= MAX and dist[nx] > time:
        dist[nx] = time
        heapq.heappush(pq, (time, nx))
    
    for nx in (x-1, x +1):
        if 0 <= nx <= MAX and dist[nx] > time + 1:
            dist[nx] = time + 1
            heapq.heappush(pq, (time + 1, nx))