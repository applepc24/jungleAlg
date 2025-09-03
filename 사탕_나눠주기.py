import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    ps = [0] * (N + 1)
    for i in range(1 , N+1):
        ps[i] = ps[i -1] + A[i - 1]

    def candies_needed(X):
        idx = bisect_right(A, X)
        cnt = N -idx
        if cnt <= 0:
            return 0
        tail_sum = ps[N] - ps[idx]
        return tail_sum - cnt*X

    lo, hi = 0, A[-1] if A else 0
    while lo < hi:
        mid = (lo + hi) // 2
        if candies_needed(mid) <= K:
            hi = mid
        else: 
            lo = mid + 1
    
    print(lo)

solve()