import sys

MOD = 1_000_000_007
input = sys.stdin.readline

T = int(input())
Ns = [int(input())for _ in range(T)]
maxN = max(Ns)

f = [0] * (maxN + 2)
if maxN >= 1:
    f[1] = 1
if maxN >= 2:
    f[2] = 2
for i in range(3, maxN + 1):
    f[i] = (f[i-1] + f[i - 2]) % MOD

print("\n".join(str(f[n]) for n in Ns))