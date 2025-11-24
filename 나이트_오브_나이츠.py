import sys
input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 1) 칸 번호 매기기: (r, c) -> idx = r*N + c
def num(r, c):
    return r*N + c

moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]
K = N*N
attack = [0] * K
# 2) 각 칸에서 나이트가 공격하는 칸들의 비트마스크 만들기
for r in range(N):
    for c in range(N):
        i = num(r,c)
        mask = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                j = num(nr, nc)
                mask |= (1 << j)
        attack[i] = mask

best = 0
# 3) 모든 부분집합 brute force
for mask in range(1 << K):
    ok = True
    score = 0
    for i in range(K):
        if mask & (1 << i):
            if mask & attack[i]:
                ok = False
                break
            r = i // N
            c = i % N
            score += A[r][c]
    if ok and score > best:
        best = score
print(best)