import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy

    if d2 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    sum_r = r1 + r2
    diff_r = abs(r1 - r2)

    if sum_r * sum_r == d2 or diff_r * diff_r == d2:
        print(1)
    elif diff_r * diff_r < d2 < sum_r * sum_r:
        print(2)
    else:
        print(0)
