import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 15
dp = [[[INF] *3 for _ in range(M)] for _ in range(N)]


for j in range(M):
    for d in range(3):
        dp[0][j][d] = cost[0][j]

for i in range(N):
    for j in range(M):
        for d in range(3):
            dj = [1, 0, -1]
            prev_j = j + dj[d]
            if 0 <= prev_j < M:
                for pd in range(3):
                    if pd != d:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][prev_j][pd] + cost[i][j])
answer = INF
for j in range(M):
    cand = min(dp[N-1][j])
    if answer > cand:
        answer = cand
print(answer)
                