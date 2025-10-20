import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
cur = [False] * N
for _ in range(M):
    cur[int(input())] = True

for _ in range(K):
    nxt = [False] * N
    for i in range(N):
        nxt[i] = (cur[(i-1) % N] != cur[(i+1) % N])
    cur = nxt
print(sum(cur))