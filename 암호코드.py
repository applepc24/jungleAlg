key = input().strip()
MOD = 10000000


if key[0] == '0':
    print(0)
    exit()

n = len(key)
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    one_digit = int(key[i - 1])
