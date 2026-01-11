import sys
input = sys.stdin.readline

n,m = map(int, input().split())

names = []
limits = []
for _ in range(n):
    name, lim = input().split()
    names.append(name)
    limits.append(int(lim))

def lower_idx(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo

ans = []
for _ in range(m):
    power = int(input())
    idx = lower_idx(limits, power)
    ans.append(names[idx])
print('\n'.join(ans))