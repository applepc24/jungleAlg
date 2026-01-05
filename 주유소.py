import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

low_price = price[0]
ans = 0
for i in range(N-1):
    if price[i] < low_price:
        low_price = price[i]
    ans += dist[i] * low_price

print(ans)