import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1,0), (0,1), (1,0), (0,-1)]

count = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    found = False
    for x, y in dirs:
        nx, ny = r + x , c + y
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                found = True
                break
    
    if not found:
        back = (d+2)%4
        bx = r + dirs[back][0]
        by = c + dirs[back][1]

        if board[bx][by] != 1:
            r, c = bx, by
        else:
            break
    else:
        d = (d+3) % 4
        dx = r + dirs[d][0]
        dy = c + dirs[d][1]

        if board[dx][dy] == 0:
            r, c = dx, dy

print(count)