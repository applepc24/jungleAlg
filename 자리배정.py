import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
    sys.exit()

visited = [[False] * (C+1) for _ in range(R+1)]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0

x,y = 1,1
visited[y][x] = True

if K == 1:
    print(x,y)
    sys.exit()

for num in range(2, K+1):
    nx = x + dirs[d][0]
    ny = y + dirs[d][1]

    if not (1 <= nx <= C and 1 <= ny <= R) or visited[ny][nx]:
        d = (d+1) % 4
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]

    x,y = nx, ny
    visited[y][x] = True
print(x,y)