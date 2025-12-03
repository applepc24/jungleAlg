import sys
input = sys.stdin.readline

grid = [input().strip() for _ in range(8)]
queens = []

for r in range(8):
    for c in range(8):
        if grid[r][c] == '*':
            queens.append((r, c))

row = set()
col = set()
diag1 = set()
diag2 = set()

vaild = True
for r, c in queens:
    if  r in row or c in col or (r-c) in diag1 or (r+c) in diag2:
        vaild = False
        break
    row.add(r)
    col.add(c)
    diag1.add(r-c)
    diag2.add(r+c)

if vaild:
    print('valid')
else:
    print('invalid')