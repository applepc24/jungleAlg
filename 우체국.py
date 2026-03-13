import sys
input = sys.stdin.readline

T = int(input())
vil = []

total = 0
for _ in range(T):
    x, a = map(int, input().split())
    vil.append((x,a))
    total += a

vil.sort()
half = (total + 1) // 2

acc = 0
for x,a in vil:
    acc += a
    if acc >= half:
        print(x)
        break

