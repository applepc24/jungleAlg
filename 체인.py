import sys

input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
L.sort()

M = N - 1
ans = 0

for x in L:
    if M <= 0:
        break
    if x <= M:
        ans += x
        M -= x + 1
    else:
        ans += M
        break
print(ans)
