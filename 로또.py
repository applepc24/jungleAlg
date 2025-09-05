import sys
input = sys.stdin.readline

T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]

max_n = max(n for n, m in cases)
max_m = max(m for n, m in cases)

dp = [[0] * (max_m + 1) for _ in range(max_n + 1)]

for x in range(1, max_m + 1):
    dp[1][x] = 1

for i in range(2, max_n + 1):
    pref = [0] * (max_m + 1)
    run = 0
    for x in range(1, max_m +1):
        run += dp[i-1][x]
        pref[x] = run
    for x in range(1, max_m + 1):
        dp[i][x] = pref[x // 2]

for n,m in cases:
    print(sum(dp[n][1: m+1]))