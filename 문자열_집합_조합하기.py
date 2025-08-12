import sys
from itertools import combinations
from collections import Counter

input = sys.stdin.readline

X = input().strip()
Y = input().strip()
Z = input().strip()
k = int(input())

def make_k_combos(s, k):
    result = set()
    n = len(s)

    for idxs in combinations(range(n), k):
        word = ''.join(s[i] for i in idxs)
        result.add(word)
    return result

setX = make_k_combos(X,k)
setY = make_k_combos(Y,k)
setZ = make_k_combos(Z,k)

cnt = Counter(setX) + Counter(setY) + Counter(setZ)

ans_list = []
for word, c in cnt.items():
    if c >= 2:
        ans_list.append(word)

ans = sorted(ans_list)

if ans:
    print("\n".join(ans))
else:
    print(-1)