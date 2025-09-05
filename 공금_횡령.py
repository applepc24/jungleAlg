import sys
input = sys.stdin.readline

N, M = map(int, input().split())

base = {}
for _ in range(N):
    a, b = input().split()
    base[a] = int(b)

count = 0
for _ in range(M):
    c, d = input().split()
    d = int(d)
    if d > base[c] * 1.05:
        count +=1

print(count)

