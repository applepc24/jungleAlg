from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lights = [[[] for _ in range(n)]for _ in range(n)]
on = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for _ in range(m):
    x,y,a,b = map(int, input().split())
    lights[x-1][y-1].append((a-1, b-1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q= deque()
    q.append((0,0))
    on[0][0] = True
    visited[0][0] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for a, b in lights[x][y]:
            if not on[a][b]:
                on[a][b] = True
                cnt += 1

                for d in range(4):
                    na , nb = a +dx[d], b+ dy[d]
                    if 0 <= na < n and 0<= nb < n and visited[na][nb]:
                        q.append((a,b))
                        visited[a][b] = True
                        break
        for d in range(4):
                    nx ,ny = a + dx[d], b + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and on[nx][ny] and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        break
    return cnt

print(bfs())