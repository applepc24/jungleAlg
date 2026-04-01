import sys
input = sys.stdin.readline

N, M = map(int, input().split())

before = [list(map(int, input().strip())) for _ in range(N)]
after =  [list(map(int, input().strip())) for _ in range(N)]

ans = 0

def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            before[i][j] = 1 - before[i][j]


for i in range(N - 2):
    for j in range(M - 2):
        if before[i][j] != after[i][j]:
            flip(i, j)
            ans += 1

if before == after:
    print(ans)
else:
    print(-1)