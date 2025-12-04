import sys
input = sys.stdin.readline

cut_length = []

n, k, m = map(int, input().split())
for _ in range(n):
    l = int(input())
    if l <= k:
        continue
    elif l < 2*k:
        cut_length.append(l-k)
    else:
        cut_length.append(l- 2*k)

if not cut_length:
    print(-1)
    sys.exit(0)


lo, hi = 1, max(cut_length)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for t in cut_length:
        cnt += t // mid
        if cnt >= m:
            break
    
    if cnt >= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

if ans > 0:
    print(ans)
else:
    print(-1)