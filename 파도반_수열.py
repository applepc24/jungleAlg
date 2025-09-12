import sys
input = sys.stdin.readline

T = int(input())
Ns = [int(input()) for _ in range(T)]

MAXN = 100
P = [0] * (MAXN + 1)
P[1] = P[2]= P[3] = 1
for i in range(4, MAXN + 1):
    P[i] = P[i-3] + P[i-2]

for n in Ns:
    print(P[n])