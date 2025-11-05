import sys
n = int(input())
w = list(map(int, input().split()))

L = w[0]
R = w[1]

for x in w[2:]:
    if L == R:
        L += x
    elif L < R:
        L += x
    else:
        R += x

diff  = abs(L - R)

if diff == 0:
    print(0)
else:
    denoms = [100, 50, 20, 10, 5, 2 , 1]
    cnt = 0
    for d in denoms:
        cnt += diff // d
        diff %= d
        if diff == 0:
            break
    print(cnt)
