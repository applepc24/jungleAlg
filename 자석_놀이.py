import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
bot = list(map(int, input().split()))

NEG = -10**30
dpT = top[0]
dpB = NEG
dpD = top[0] + bot[0]

for j in range(1, N):
    valT = top[j]
    valB = bot[j]
    valD = valT + valB

    nT = max(dpT, dpD) + valT
    nB = max(dpB, dpD) + valB
    nD = max(dpT, dpB, dpD) + valD

    dpT, dpB, dpD = nT, nB, nD

print(max(dpB, dpD))