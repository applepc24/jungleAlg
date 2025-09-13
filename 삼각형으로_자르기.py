import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]

def tri(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return abs((x2 - x1) * (y3 -y1) - (y2 -y1) * (x3 -x1))

best = 0

for i, j, k in combinations(range(N) , 3):
    best = max(best, tri(S[i], S[j], S[k]))

print(best /2)
