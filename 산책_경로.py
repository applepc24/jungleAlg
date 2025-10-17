import sys
import math

input = sys.stdin.readline
N = int(input())

S = []
sx = sy = 0
for _ in range(N):
    x, y = map(int, input().split())
    S.append((x,y))
    sx += x
    sy += y
print(sx, sy)
best = float('inf')
for x, y in S:
    nx = sx -x
    ny = sy -y
    d = math.sqrt((nx * nx) + (ny * ny))
    best = min(d, best)

print(f"{best:.2f}")
