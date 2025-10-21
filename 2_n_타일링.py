import sys
input = sys.stdin.readline

n = int(input())
mod = 10007

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a+b) % mod
    print(b)