import sys
input = sys.stdin.readline
n, C = map(int, input().split())
t = list(map(int, input().split()))
x = list(map(int, input().split()))

lo, hi = 0, max(x)

def check(R):
    water = 0
    for i in range(n):
        water += (x[i] - R) * t[i]
        if water > C:
            return False 
        
        if water < 0:
            water = 0
    return True



for _ in range(80):
    mid = (lo + hi) /2
    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)
