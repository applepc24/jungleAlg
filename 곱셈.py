import sys

input = sys.stdin.readline

a,b,c = list(map(int, input().split()))

def mod_pow(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result

print(mod_pow(a,b,c))

 