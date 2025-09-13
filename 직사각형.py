import sys
import math

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N = int(input())

    a1= math.isqrt(N)
    b1 = math.ceil(N / a1)
    p1 = 2*(a1+b1)

    a2 = a1 + 1
    b2 = math.ceil(N / a2)
    p2 = 2 * (a2 + b2)
    ans.append(str(min(p1, p2)))

print('\n'.join(ans))
     
