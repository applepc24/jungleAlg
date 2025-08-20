import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n + 1):
        if i + 1 <= n:
            dp[i+1] = min(dp[i+1], dp[i] + 1)
        j = i + i // 2
        if j <= n:
            dp[j] = min(dp[j], dp[i] + 1)
    print("minigimbob" if dp[n] <= k else "water" )

solve()