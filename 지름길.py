import sys
input = sys.stdin.readline

n, d = map(int, input().split())
INF = 10**9

shortcuts = [[] for _ in range(d+1)]

for _ in range(n):
    s,e,l = map(int, input().split())
    if e <= d:
        shortcuts[s].append((e,l))

dp = [INF] * (d+1)
dp[0] = 0
for x in range(d):
    dp[x+1] = min(dp[x+1], dp[x] + 1)
    for e,l in shortcuts[x]:
        dp[e] = min(dp[e], dp[x] + l)

print(dp[d])