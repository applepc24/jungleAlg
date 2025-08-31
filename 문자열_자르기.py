import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
cuts = list(map(int, input().split()))

cuts = [0] + sorted(cuts) + [n]
dp = [[0] * (m+2) for _ in range(m+2)]

for length in range(2, m+2):
    for i in range(m+2 - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i+1, j):
            cost = dp[i][k] + dp[k][j] + cuts[j] -cuts[i]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][m+1])


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cuts = list(map(int, input().split()))
cuts = [0] + sorted(cuts) + [n]

dp = [[0] * (m+2) for _ in range(m+2)]
opt = [[0] * (m+2) for _ in range(m+2)]

for i in range(m+1):
    opt[i][i+1] = i + 1

for length in range(2, m+2):
    for i in range(m+2 - length):
        j = i + length
        dp[i][j] = float('inf')
        # k 범위를 최적화
        for k in range(opt[i][j-1], opt[i+1][j] + 1):
            cost = dp[i][k] + dp[k][j] + cuts[j] - cuts[i]
            if cost < dp[i][j]:
                dp[i][j] = cost
                opt[i][j] = k

print(dp[0][m+1])