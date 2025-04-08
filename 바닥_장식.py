import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y, pic):
    visited[x][y] = True
    if pic == '-':
        plus_y = y + 1
        if 0 <= plus_y < m and not visited[x][plus_y] and map[x][plus_y] == '-':
            dfs(x,plus_y,pic)
    elif pic == '|':
        plus_x = x +1
        if 0 <= plus_x < n and not visited[plus_x][y] and map[plus_x][y] == '|':
             dfs(plus_x,y,pic)
       

count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i, j, map[i][j])
            count += 1

print(count)

# 이 문제는 어디서 뭐가 틀렸는지 모르겠어 y + 1해주는게 아닌가?