import sys
input = sys.stdin.readline

N = int(input())
R,C = map(int, input().split())

if N == 3:
    if R ==2 and C == 2:
        print(1)
    else:
        print(4)
else:
    total = N*N
    if (R+C) % 2 == 0:
        print((total + 1) // 2)
    else:
        print(total // 2)