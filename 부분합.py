import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

INF = 10**9
ans = INF

L = 0
cur_sum = 0

for r in range(N):
    cur_sum += arr[r]

    while cur_sum >= S:
        ans = min(ans, r - L + 1)
        cur_sum -= arr[L]
        L += 1

if ans == INF:
    print(0)
else:
    print(ans)