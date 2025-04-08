import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for child in tree[node]:
        if parent[child] == 0:
            parent[child] = node
            dfs(child)

dfs(1)

for i in range(2, N+1):
    print(parent[i])

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
    # 상 , 하, 좌, 우
dx = [-1, 1,  0,  0]
dy = [ 0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n-1][m-1]

print(bfs(0,0))