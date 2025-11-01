import sys
input = sys.stdin.readline



MAX = 1_000_000
f = [0] * (MAX + 1)
for d in range(1, MAX + 1):
    for m in range(d, MAX + 1, d):
        f[m] += d

g = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    g[i] = g[i-1] + f[i]

T = int(input())
out = []
for _ in range(T):
    n = int(input())
    out.append(str(g[n]))

print('\n'.join(out))