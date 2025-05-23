from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

move = [[-2,-1],[-2,+1],[0,-2],[0,+2],[+2,-1],[+2, +1]]

def bfs():
    visited = [[-1]*n for _ in range(n)]
    visited[r1][c1] = 0

    queue = deque()
    queue.append((r1, c1))

    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return visited[x][y]
        for dx, dy in move:
            nx, ny = x + dx, y +dy
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1

print(bfs())

