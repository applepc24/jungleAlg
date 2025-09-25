R, C = map(int, input().split())
map = [list(input().strip()) for _ in range(R)]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def is_road(r, c):
    return 0 <= r < R and 0 <= c < C and map[r][c] == '.'

end = False
for r in range(R):
    for c in range(C):
        if map[r][c] != '.':
            continue
        deg = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if is_road(nr, nc):
                deg += 1
        if deg <= 1:
            end = True
    if end:
        break
print(1 if end else 0)
     

        