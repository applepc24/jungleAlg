from collections import deque

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

visited_normal = [[False] * n for _ in range(n)]
visited_weak = [[False] * n  for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y, visited, board):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    color = board[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

normal_count = 0
for i in range(n):
    for j in range(n):
        if not visited_noraml[i][j]:
            bfs(i, j, visited_noraml, graph)
            normal_count += 1

weak_graph = [['R' if c == 'G' else c for c in row] for row in graph]

weak_count = 0
for i in range(n):
    for j in range(n):
        if not visited_weak[i][j]:
            bfs(i,j,visited_weak, weak_graph)
            weak_count += 1

print(normal_count, weak_count)