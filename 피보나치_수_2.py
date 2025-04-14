import sys
input = sys.stdin.readline

n = int(input())

def fibo(n , memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]