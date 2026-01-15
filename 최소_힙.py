import sys
import heapq
input = sys.stdin.readline

n = int(input())


heap = []
out = []
for _ in range(n):
    x = int(input())
    
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            out.append(str(heapq.heappop(heap)))
        else:
            out.append('0')

print('\n'.join(out))