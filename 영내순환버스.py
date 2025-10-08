import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
t = list(map(int, input().split()))

offset = [0] * (N + 1)
for s in range(2, N+1):
    offset[s] = offset[s-1] + t[s-2]
T= sum(t)

ans = 0

for _ in range(M):
    p, r, c = map(int, input().split())
    off_p = offset[p]
    if c <= off_p:
        k = 0
    else:
        k = (c - off_p + T -1) //T

    board = off_p + k*T
    delta = (offset[r] - offset[p]) % T
    alight = board + delta

    if alight > ans:
        ans = alight

print(ans)

