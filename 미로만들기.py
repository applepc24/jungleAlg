from collections import deque

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[-1] * n for _  in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n:
                if visited[nx][ny] == -1:
                    if maze[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

bfs()
print(visited[n-1][n-1])