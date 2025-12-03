import bisect
import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

# 26개 리스트: 각 알파벳이 등장한 인덱스들을 저장
pos = [[] for _ in range(26)]

for i, ch in enumerate(S):
    idx = ord(ch) - ord('a')
    pos[idx].append(i)

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l); r = int(r)
    idx = ord(alpha) - ord('a')
    arr = pos[idx]

    left = bisect.bisect_left(arr, l)
    right = bisect.bisect_right(arr, r)
    print(right - left)

