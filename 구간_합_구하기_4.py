import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

prefix = [0] * (N+1)

for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + num[i-1]

R = [tuple(map(int, input().split())) for _ in range(M)]
out = []
for i, j in R:
    out.append(str(prefix[j] - prefix[i-1]))

print('\n'.join(out))