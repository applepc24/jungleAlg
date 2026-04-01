import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    print(a * 10)

