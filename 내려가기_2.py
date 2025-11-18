import sys
input = sys.stdin.readline
N = int(input())
a0, a1 ,a2 = map(int, input().split())
max_dp = [a0, a1, a2]
min_dp = [a0, a1, a2]

for _ in range(N - 1):
    b0, b1, b2 = map(int, input().split())

    max0 = b0 + max(max_dp[0] , max_dp[1])
    max1 = b1 + max(max_dp[1], max_dp[0], max_dp[2])
    max2 = b2 + max(max_dp[1], max_dp[2])

    min0 = b0 + min(min_dp[0], min_dp[1])
    min1 = b1 + min(min_dp[0], min_dp[1], min_dp[2])
    min2 = b2 + min(min_dp[1], min_dp[2])

    max_dp = [max0, max1, max2]
    min_dp = [min0, min1, min2]

print(max(max_dp), min(min_dp))
