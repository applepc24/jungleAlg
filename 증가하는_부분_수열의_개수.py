import sys
input = sys.stdin.readline
N = int(input())
A= list(map(int, input().split()))
A = [0] + A
dp = [0] * (N + 1)
mod = 998244353

for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if A[j] < A[i]:
            dp[i] += dp[j]
        dp[i] %= mod

print(*dp[1:])