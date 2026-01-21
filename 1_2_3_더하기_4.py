import sys
input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]
max_num = max(nums)

dp = [0] * (max_num + 1)
dp[0] = 1

for coin in (1, 2, 3):
    for x in range(coin, max_num + 1):
        dp[x] += dp[x - coin]

for n in nums:
    print(dp[n])