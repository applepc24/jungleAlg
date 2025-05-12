board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

def winner(x, y, color, dir):
    # 앞쪽 돌이 있으면 중복 오목이므로 패스
    px, py = x - dx[dir], y - dy[dir]
    if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == color:
        return False

    cnt = 1
    nx, ny = x + dx[dir], y + dy[dir]
    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
        cnt += 1
        nx += dx[dir]
        ny += dy[dir]
    
    return cnt == 5

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for d in range(4):
                if winner(i, j, board[i][j], d):
                    print(board[i][j])
                    print(i + 1, j + 1)
                    exit()
print(0)