import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [tuple(map(int, input().split())) for _ in range(k)]

dp = [0] * (T + 1)
dp[0] = 1

for p, n in coins:
    ndp = [0] * (T + 1)
    for t in range(T + 1):
        if dp[t] == 0:
            continue
        max_cnt = min(n, (T - t) // p)
        for cnt in range(max_cnt + 1):
            ndp[t + cnt*p] += dp[t]
    dp = ndp

print(dp[T])