import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

def can_place(dist: int) -> bool:
    cnt = 1
    last = houses[0]

    for x in houses[1:]:
        if x - last >= dist:
            cnt += 1
            last = x
    return cnt >= C

lo, hi = 1, houses[-1] - houses[0]
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_place(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)