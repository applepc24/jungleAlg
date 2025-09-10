import sys
from itertools import combinations

input = sys.stdin.readline

n, m, k = map(int, input().split())
quests = []
for _ in range(m):
    need = list(map(int, input().split()))
    mask = 0
    for x in need:
        mask |= 1 << (x-1)
    quests.append(mask)
best = 0
S = 2 * n

for comb in combinations(range(S), n):
    sel = 0
    for b in comb:
        sel |= 1 << b
    
    cnt = 0
    for q in quests:
        if (sel & q) == q:
            cnt += 1
    
    if cnt > best:
        best = cnt

print(best)

