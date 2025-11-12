import sys
input = sys.stdin.readline
from bisect import bisect_left

N, M, X = map(int, input().split())
a = list(map(int, input().split()))

cheap = a[-1]
R = N
B = X
cnt = [0] * M

b = [-x for x in a]

while R > 0:
    T = B - (R -1) * cheap

    k = bisect_left(b, -T)
    p = a[k]

    if p == cheap:
        cnt[k] += R
        break

    lo, hi = 1, R
    best_t  = 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if B - mid *p >= (R-mid) * cheap:
            best_t = mid
            lo = mid + 1
        else:
            hi = mid - 1
    t = best_t
    cnt[k] += t
    R -= t
    B -= t * p

print(*cnt)