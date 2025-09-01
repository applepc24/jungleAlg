import sys
import bisect

input = sys.stdin.readline

N = int(input().strip())
xs = []
ys = []

for i in range(N):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)

Q = int(input().strip())

for _ in range(Q):
    k = float(input().strip())

    right = bisect.bisect_right(xs, k)
    left = right - 1

    dy = ys[right] - ys[left]

    if dy > 0:
        print(1)
    elif dy <  0:
        print(-1)
    else:
        print(0)

