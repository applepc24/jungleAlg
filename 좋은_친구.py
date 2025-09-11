import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

freq = [0] * 21
window = deque()
ans = 0

for _ in range(N):
    name = input().strip()
    L = len(name)

    ans += freq[L]

    freq[L] += 1
    window.append(L)

    if len(window) > K:
        old = window.popleft()
        freq[old] -= 1
print(ans)

    