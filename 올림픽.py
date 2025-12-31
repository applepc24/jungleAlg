import sys
input = sys.stdin.readline
N, K = map(int, input().split())

medal = {}
for _ in range(N):
    i, g, s, b = map(int, input().split())
    medal[i] = (g,s,b)



better = 0
for i in medal:
    if medal[i] > medal[K]:
        better += 1

print(better +1)