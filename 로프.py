import sys
input = sys.stdin.readline

N = int(input())

roaf = [int(input()) for _ in range(N)]
roaf.sort()

max_up = 0

for i in range(N):
    weigh = roaf[i] * (N-i)
    max_up = max(weigh, max_up)

print(max_up)