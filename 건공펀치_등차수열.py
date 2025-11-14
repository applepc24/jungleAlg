import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A= list(map(int, input().split()))

base = -10**18
for i in range(N):
    candi = A[i] -i*K
    if candi >= base:
        base = candi

total_punch = 0
for i in range(N):
    target = base + i*K
    total_punch += target - A[i]

print(total_punch)