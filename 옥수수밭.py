import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

pq = []
seen = [[False] * M for _ in range(N)]
taken = [[False] * M for _ in range(N)]

def push_if_new(r, c):
    if 0 <= r < N and 0 <= c < M and not seen[r][c]:
        seen[r][c] = True
        heapq.heappush(pq, (-A[r][c], r, c))

for c in range(M):
    push_if_new(0, c)
    if N > 1:
        push_if_new(N-1 ,c)
for r in range(N):
    push_if_new(r, 0)
    if M > 1:
        push_if_new(r, M -1)

out = []
cnt = 0
while cnt < K and pq:
    negv, r, c = heapq.heappop(pq)
    if taken[r][c]:
        continue
    taken[r][c] = True
    out.append(f"{r+1} {c+1}")
    cnt +=1

    push_if_new(r-1, c)
    push_if_new(r+1, c)
    push_if_new(r, c-1)
    push_if_new(r, c+1)

print("\n".join(out)) 