import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a, s))
    
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[c] = 0

    heap = [(0, c)]
    while heap:저ㅏ 저ㅏ
        time, node = heapq.heappop(heap)
        if dist[node] < time:
            continue
        for next_node, cost in graph[node]:
            if dist[next_node] > time + cost:
                dist[next_node] = time + cost
                heapq.heappush(heap, (dist[next_node], next_node))
    count =  sum(1 for t in dist if t != INF)
    max_time = max([t for t in dist if t != INF])
    print(count, max_time)