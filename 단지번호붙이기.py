import sys
input = sys.stdin.readline
n = int(input())

graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x,y):
    visited[x][y] = True
    count = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny <n:
            if graph[nx][ny] == '1' and not visited[nx][ny]:
                count += dfs(nx, ny)
    
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            result.append(dfs(i,j))

result.sort()

print(len(result))
for cnt in result:
    print(cnt)
            

                
