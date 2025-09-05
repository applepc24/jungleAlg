import sys
input = sys.stdin.readline

N, T = map(int, input().split())

turns = []
for _ in range(N):
    ti, si = input().split()
    turns.append((int(ti), si))

dir = 0
x=y=0
prev_t = 0

def turn(dt, dir, x, y):
    if dir == 0:
        x += dt
    elif dir == 1:
        y += dt
    elif dir == 2:
        x -= dt
    elif dir == 3:
        y -= dt
    return x, y

for ti, si in turns:
    dt = ti - prev_t
    if dt > 0:
        x, y = turn(dt, dir, x, y)
    prev_t = ti

    if si == "left":
        dir = (dir + 1) % 4
    else:
        dir =(dir + 3) % 4
    
if T > prev_t:
    x, y = turn(T-prev_t , dir, x, y)

print(x, y)