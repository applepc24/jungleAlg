import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    board = [list(input().strip()) for _ in range(3)]
    player =  input().strip()

    found = False

    for r in range(3):
        row = board[r]
        if row.count(player) == 2 and row.count('-') == 1:
            c = row.index('-')
            board[r][c] = player
            found = True
            break

    if not found:
        for c in range(3):
            col = [board[r][c] for r in range(3)]
            if col.count(player) == 2 and col.count('-') == 1:
                r = col.index('-')
                board[r][c] = player
                found = True
                break
    
    if not found:
        diag = [board[i][i] for i in range(3)]
        if diag.count(player) == 2 and diag.count('-') == 1:
            i = diag.index('-')
            board[i][i] = player
            found = True
            
            
    if not found:
        diag = [board[i][2- i] for i in range(3)]
        if diag.count(player) == 2 and diag.count('-') == 1:
            i= diag.index('-')
            board[i][2-i] = player
            found = True
            

    print(f"Case {t}:")
    for row in board:
        print(''.join(row))