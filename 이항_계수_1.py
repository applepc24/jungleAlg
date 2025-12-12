import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def fact(x):
    r = 1
    for i in range(2, x+1):
        r *= i
    return r

ans = fact(N) // (fact(K) * fact(N - K))
print(ans)
