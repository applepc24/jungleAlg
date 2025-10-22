import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

EVEN = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, 0), (1, -1)]
ODD  = [(-1, 0), (-1,  1), (0, -1), (0, 1), (1, 0), (1,  1)]

ans = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] != '#':
            continue
        
        dirs = EVEN if (r % 2 == 0) else ODD
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '.':
                    ans +=1
print(ans)