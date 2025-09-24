R, C =  map(int, input().split())
G = [list(input().strip()) for _ in range(R)]

dirs = [(-1,0), (1,0), (0,-1),(0,1)]

def is_road(r, c):
    return 0 <= r < R and 0 <= c < C and G[r][c] == '.'

dead_end = False
for r in range(R):
    for c in range(C):
        if G[r][c] != '.':
            continue
        deg = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if is_road(nr, nc):
                deg += 1
        if deg <= 1:
            dead_end = True
    if dead_end:
        break

print(1 if dead_end else 0)