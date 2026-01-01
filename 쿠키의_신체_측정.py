import sys
input = sys.stdin.readline

N = int(input())
grid = [input().strip() for _ in range(N)]

head_x = head_y = -1
found = False

for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            head_x, head_y = i , j 
            found = True
            break
    if found:
        break
heart_x, heart_y = head_x + 1, head_y

def count_left(x,y):
    cnt = 0
    y -= 1
    while  y >= 0 and grid[x][y] == '*':
        cnt += 1
        y -= 1
    return cnt

def count_right(x,y):
    cnt = 0
    y += 1
    while y < N and grid[x][y] == "*":
        cnt += 1
        y += 1
    return cnt

def count_down(x, y):
    cnt = 0
    x += 1
    while x < N and grid[x][y] == '*':
        cnt += 1
        x += 1
    return cnt

leftarm = count_left(heart_x, heart_y)
rightarm = count_right(heart_x, heart_y)
waist = count_down(heart_x, heart_y)

waist_end_x = heart_x + waist
left_leg = 0
right_leg = 0

lx, ly = waist_end_x + 1, heart_y - 1
rx, ry = waist_end_x + 1, heart_y + 1

while lx < N and grid[lx][ly] == '*':
    left_leg += 1
    lx += 1

while rx < N and grid[rx][ry] == "*":
    right_leg += 1
    rx += 1

print(heart_x + 1, heart_y + 1)
print(leftarm, rightarm, waist, left_leg, right_leg)