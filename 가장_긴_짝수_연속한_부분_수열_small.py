import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

best = 0
L = 0
odd = 0
even = 0

for R in range(N):
    if S[R] % 2 == 0:
        even += 1
    else:
        odd +=1

    while odd > K:
        if S[L] % 2 == 0:
            even -= 1
        else:
            odd -= 1
        L += 1
    best = max(best, even)
print(best)