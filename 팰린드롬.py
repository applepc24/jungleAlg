import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    if arr[i] == arr[i + 1]:
        dp[i][i+1] = 1

for length in range(3, n+1):
    for s in range(1, n- length +2):
        e = s+ length -1
        if arr[s] == arr[e] and dp[s+1][e-1]:
            dp[s][e] =1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])