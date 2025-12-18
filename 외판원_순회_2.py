import sys
input = sys.stdin.readline

INF = 10**9
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[INF] * N for _ in range(1 << N)]
ALL = (1 << N) -1
dp[1][0] = 0

for mask in range(1 << N):
    for i in range(N):
        if dp[mask][i] == INF:
            continue
        if not (mask & (1 << i)):
            continue
        
        for j in range(N): 
            if mask & (1 << j):
                continue
            if W[i][j] == 0:
                continue
            
            nmask = mask | (1 << j)
            dp[nmask][j] = min(dp[nmask][j], dp[mask][i] + W[i][j])

ans = INF
for i in range(N):
    if dp[ALL][i] == INF:
        continue
    if W[i][0] == 0:
        continue
    ans = min(ans , dp[ALL][i] + W[i][0])
print(ans)