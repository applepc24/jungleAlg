import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1
    
    found = False
    for x, y in dirs:
        nr, nc = r + x, c + y
        if board[nr][nc] == 0:
            found = True
            break
    
    if not found:
        back = (d + 2) % 4
        br = r + dirs[back][0]
        bc = c + dirs[back][1]

        if board[br][bc] != 1:
            r, c = br, bc
        else:
            break
    else:
        d = (d + 3) % 4
        nr = r + dirs[d][0]
        nc = c + dirs[d][1]

        if board[nr][nc] == 0:
            r, c = nr, nc

print(count)