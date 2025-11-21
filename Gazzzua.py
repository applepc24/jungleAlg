import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

profit = 0
max_price = 0
for i in range(N-1, -1, -1):
    price = arr[i]
    if price > max_price:
        max_price = price
    else:
        profit += max_price - price
print(profit)

