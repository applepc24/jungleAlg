import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]

dirs = [(1,0), (0,1), (-1,0), (0,-1)]
ans = 0

seen = [[set() for _ in range(c)] for _ in range(r)]

def dfs(x,y,mask,depth):
    global ans
    if depth > ans:
        ans = depth

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < r and 0 <= ny < c:
            ch = ord(board[nx][ny]) - ord('A')
            bit = 1 << ch
            if mask & bit:
                continue
            
            nmask = mask | bit

            if nmask in seen[nx][ny]:
                continue
            seen[nx][ny].add(nmask)

            dfs(nx,ny,nmask,depth+1)

start_mask = 1 << (ord(board[0][0]) - ord('A'))
seen[0][0].add(start_mask)
dfs(0,0,start_mask, 1)
print(ans)