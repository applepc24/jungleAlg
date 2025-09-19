import sys, math

input= sys.stdin.readline
N = int(input())

if N == 1:
    print(0)
else:
    p = None
    limit = math.isqrt(N)
    for i in range(2, limit + 1):
        if N % i == 0:
            p = i
            break
    
    if p is None:
        d = 1
    else:
        d= N //p
    print(N -d)