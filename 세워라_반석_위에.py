from collections import deque
N = int(input())
A = list(map(int, input().split()))

maxdq, mindq = deque(), deque()
L = 0
best = 0

for R, i in enumerate(A):
    while maxdq and A[maxdq[-1]] < i:
        maxdq.pop()
    maxdq.append(R)

    while mindq and A[mindq[-1]] > i:
        mindq.pop()
    mindq.append(R)

    while A[maxdq[0]] - A[mindq[0]] > 2:
        if maxdq[0] == L:
            maxdq.popleft()
        if mindq[0] == L:
            mindq.popleft()
        L += 1
    best = max(best, R - L + 1)
print(best)