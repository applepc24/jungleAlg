import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

cntR = S.count('R')
cntU = S.count('U')
cntX = S.count('X')

K = int(input())

ans = 0

for _ in range(K):
    x, y = map(int, input().split())
    dx = x - 1
    dy = y - 1

    L = max(0, dx- cntR, dy - cntU)
    R = min(cntX, dx, dy)

    if L <= R:
        ans += 1
print(ans)