import sys
import bisect

input = sys.stdin.readline

n,m = map(int, input().split())

A = [int(input()) for _ in range(n)]
B = sorted(A)

for _ in range(m):
    d = int(input())
    idx = bisect.bisect_left(B, d)
    if idx < n and B[idx] == d:
        print(idx)
    else:
        print(-1)