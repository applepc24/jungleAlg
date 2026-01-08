import sys
input = sys.stdin.readline

x,y,w,s = map(int, input().split())

cost1 = (x+y) * w

a = max(x,y)
b = min(x, y)
cost2 = (b * s) + (a-b) * w

if (a-b) % 2 == 0:
    cost3 = a * s
else:
    cost3 = ((a-1) * s) + w

print(min(cost1, cost2, cost3))