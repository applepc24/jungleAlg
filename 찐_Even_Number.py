import sys
input = sys.stdin.readline
Q = int(input())

mod = 10 ** 9 + 7
for _ in range(Q):
    N = int(input())

    if N == 1:
        print(5)
    else:
        ways = 4* pow(5, N-1, mod)
        ways %= mod
        print(ways)

        
