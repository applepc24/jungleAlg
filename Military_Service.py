import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N,K = map(int, input().split())
    print((N*K)//(K+1))
