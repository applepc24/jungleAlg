import sys

input = sys.stdin.readline

N, K = map(int, input().split())

buckets = []
for _ in range(N):
    g, x = map(int, input().split())
    buckets.append((x, g))

buckets.sort()

l = 0
cur_sum = 0
best = 0

for r in range(N):
    xr, gr = buckets[r]
    cur_sum += gr

    while buckets[r][0] - buckets[l][0] > 2*K:
        xl, gl = buckets[l]
        cur_sum -= gl
        l += 1
    
    if cur_sum > best:
        best = cur_sum
print(best)