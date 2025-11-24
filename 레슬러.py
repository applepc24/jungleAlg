import sys
input = sys.stdin.readline
from functools import cmp_to_key

N = int(input())
players = []
for i in range(1, N + 1):
    s, r = map(int, input().split())
    players.append((i, s, r))

def cmp(a,b):
    _, sa, ra = a
    _, sb, rb = b
    left = (ra-1) * sb
    right = (rb-1) * sa

    if left > right:
        return -1
    else:
        return 1

players.sort(key= cmp_to_key(cmp))

for i, _, _, in players:
    print(i)
