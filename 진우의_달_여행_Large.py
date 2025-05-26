import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[[INF] * 3 for _ in range(m)]for _ in range(n)]

for j in range(m):
    for d in range(3):
        dp[0][j][d] = fuel[0][j]

for i in range(1, n):
    for j in range(m):
        for d in range(3):
            prev_j = j + (d - 1)
            if 0 <= prev_j < m:
                for pd in range(3):
                    if pd != d:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][prev_j][pd] + fuel[i][j])

answer = INF
for j in range(m):
    for d in range(3):
        answer = min(answer, dp[n-1][j][d])

print(answer)
