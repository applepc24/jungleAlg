import sys
input = sys.stdin.readline

wins = [(0,1,2), (3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]

def is_win(w, ch):
    for a,b1,c in wins:
        if w[a] == ch and w[b1] == ch and w[c] == ch:
            return True
    return False

while True:
    s = input().strip()
    if s == 'end':
        break

    x = s.count('X')
    o = s.count('O')

    if not (x == o or x == o+1):
        print('invalid')
        continue

    x_win = is_win(s, 'X')
    o_win = is_win(s, 'O')

    if x_win and o_win:
        print('invalid')
        continue

    if x_win:
        print('valid' if x == o+1 else 'invalid')
    elif o_win:
        print('valid' if x == o else 'invalid')
    else:
        print('valid' if "." not in s else "invalid")