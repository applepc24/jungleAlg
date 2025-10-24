import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0
    d= 5
    while d <= n:
        cnt += n // d
        d *= 5
    print(cnt)