import sys
input = sys.stdin.readline

N, K = map(int, input().split())
mod =  1_000_000_000

dp = [[0] * (N+1) for _ in range(K+1)]
for n in range(N+1):
    dp[1][n] = 1

for k in range(1, K + 1):
    dp[k][0] = 1

for k in range(2, K+1):
    for n in range(1, N+1):
        dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % mod

print(dp[K][N])
