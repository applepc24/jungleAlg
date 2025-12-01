import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
q = int(input())

cnt = [[0] * (n + 1) for _ in range(26)]

for i, ch in enumerate(S):
    idx = ord(ch) - ord('a')
    for c in range(26):
        cnt[c][i + 1] = cnt[c][i]

    cnt[idx][i + 1] += 1

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    c_idx = ord(alpha) - ord('a')
    print(cnt[c_idx][r + 1] - cnt[c_idx][l])


