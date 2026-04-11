import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)

for _ in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    s = a+b
    heapq.heappush(arr, s)
    heapq.heappush(arr, s)

print(sum(arr))