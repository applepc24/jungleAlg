import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0][0] = 1

for t in range(1, M+1):
    for i in range(1, N+1):
        if i -1 >= 0 and dp[i-1][t-1] != -1:
            dp[i][t] =  max(dp[i][t], dp[i-1][t-1] + A[i])

        if i - 2 >= 0 and dp[i-2][t-1] != -1:
            dp[i][t] = max(dp[i][t], (dp[i-2][t-1] // 2) + A[i])

ans = 0
for i in range(N+1):
    for t in range(M+1):
        ans = max(ans, dp[i][t])

print(ans)