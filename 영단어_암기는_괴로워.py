import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
words = (input().strip() for _ in range(N))

arr = []
for w in words:
    if len(w) >= M:
        arr.append(w)

cnt = Counter(arr)


def sort_key(w):
    return (-cnt[w], -len(w), w)

sorted_word = sorted(cnt, key= sort_key)
print("\n".join(sorted_word))