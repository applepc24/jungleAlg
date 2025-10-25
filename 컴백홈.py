import sys
input = sys.stdin.readline


R,C,K = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0

sr, sc = R-1, 0
fr, fc = 0 , C-1

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(r, c, dist):
    global ans
    if r == fr and c == fc:
        if dist == K:
            ans += 1
        return
    
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] == '.' and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, dist + 1)
                visited[nr][nc] = False

if grid[sr][sc] == '.' and grid[fr][fc] == '.':
    visited[sr][sc]=True
    dfs(sr,sc,1)

print(ans)
