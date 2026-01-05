import sys
N = int(input())
M = int(input())
pos = list(map(int, input().split()))

def can(h:int) -> bool:
    reach = 0
    for x in pos:
        left = x - h
        right = x + h
        if left > reach:
            return False
        if right > reach:
            reach = right
        if reach >= N:
            return True
    return reach >= N

lo , hi = 0, N
ans = N
while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid):
        ans = mid
        hi = mid -1
    else:
        lo = mid + 1

print(ans)

