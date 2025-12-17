N = int(input())
coins = [500, 100, 50, 10, 5, 1]
money = 1000 - N


cnt = 0
for c in coins:
    cnt += money // c
    money = money % c

print(cnt)
