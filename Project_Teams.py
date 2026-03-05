import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))
W.sort()

G = []
for i in range(N):
    G.append(W[i] + W[2*N -1 - i])

print(min(G))