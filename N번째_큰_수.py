import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    for x in map(int, input().split()):
        heapq.heappush(heap, x)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])
