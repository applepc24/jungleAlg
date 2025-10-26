import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
seat = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if j + K <= M:
            if sum(seat[i][j:j+K]) == 0:
                cnt += 1

print(cnt)