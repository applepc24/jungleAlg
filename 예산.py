import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

if sum(arr) <= M:
    print(max(arr))
    sys.exit()

lo, hi = 0, max(arr)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    total = 0
    for x in arr:
        if x < mid:
            total += x
        else:
            total += mid
    if total <= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
