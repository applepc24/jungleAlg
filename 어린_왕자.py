import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    sx, sy, fx, fy = map(int, input().split())
    N = int(input())
    cnt = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        dist1 = (cx - sx) ** 2 + (cy - sy) ** 2
        dist2 = (cx - fx) ** 2  + (cy - fy) ** 2
        r2 = r ** 2

        inside_start = dist1 < r2
        inside_end = dist2 < r2

        if inside_start and not inside_end:
            cnt += 1
        elif inside_end and not inside_start:
            cnt += 1
    print(cnt)