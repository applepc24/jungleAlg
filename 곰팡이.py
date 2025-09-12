from collections import deque
import sys

input = sys.stdin.readline

def inside(y, x, h, w):
    return 0 <= y < h and 0 <= x < w

def count_components(arr):
    h, w = len(arr), len(arr[0])
    vis = [[False] * w for _ in range(h)]
    comps = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] > 0 and not vis[i][j]:
                comps += 1
                q = deque([(i,j)])
                vis[i][j] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in [(-1, 0), (1,0), (0,-1), (0, 1)]:
                        ny, nx = y + dy, x + dx
                        if inside(ny, nx, h, w) and arr[ny][nx] > 0 and not vis[ny][nx]:
                            vis[ny][nx] = True
                            q.append((ny, nx))
    return comps

def spread_one_day(arr):
    h,w = len(arr), len(arr[0])
    nar = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            s = arr[y][x]
            if s == 0:
                continue
            nar[y][x] = max(nar[y][x], s)
            for ny in range(y - s, y + s + 1):
                if ny < 0 or ny >= h:
                    continue
                for nx in range(x -s, x + s + 1):
                    if 0 <= nx < w:
                        nar[ny][nx] = max(nar[ny][nx] ,s)
    return nar

def solve():
    m, n = map(int, input().split())
    grid = [list(map(int, input().strip())) for _ in range(m)]
    day =0
    
    if count_components(grid) <= 1:
        print(0)
        return
    
    while True:
        day += 1
        grid = spread_one_day(grid)
        if count_components(grid) == 1:
            print(day)
            return

solve()