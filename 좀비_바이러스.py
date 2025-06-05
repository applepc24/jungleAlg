import heapq

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

visited = [[(0,-1)]*M for _ in range(N)]

q= []
for i in range(N):
    for j in range(M):
        if maps[i][j] in [1,2]:
            virus = maps[i][j]
            heapq.heappush(q,(0,virus,i,j))
            visited[i][j] = (virus, 0)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    time, virus, x, y = heapq.heappop(q)
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != -1:
            prev_virus, prev_time = visited[nx][ny]

            if prev_virus == 0:
                visited[nx][ny] = (virus, time +1)
                maps[nx][ny] = virus
                heapq.heappush(q, (time +1, virus, nx, ny))
                
            elif prev_virus != virus and prev_time == time + 1 and maps[nx][ny] != 3:
                maps[nx][ny] = 3
                visited[nx][ny] = (3, time + 1)

count = [0, 0, 0, 0]
for i in range(N):
    for j in range(M):
        if maps[i][j] in [1, 2, 3]:
            count[maps[i][j]] += 1

print(count[1],count[2], count[3])
