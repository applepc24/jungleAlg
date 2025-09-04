import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
items = [tuple(map(int, input().split())) for _ in range(N)]

heap1 = [(-q, p, q, p) for q, p in items]
heapq.heapify(heap1)
first = heapq.heappop(heap1)
second = heapq.heappop(heap1)
print(first[2], first[3], second[2], second[3])

heap2 = [(p, -q, q, p) for q, p in items]
heapq.heapify(heap2)
first = heapq.heappop(heap2)
second = heapq.heappop(heap2)
print(first[2], first[3], second[2], second[3])