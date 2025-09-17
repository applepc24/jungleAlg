import sys

def dist2(ax, ay, bx, by):
    dx = ax -bx
    dy = ay - by
    return dx*dx + dy*dy

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    targets = [tuple(map(int, input().split())) for _ in range(N)]
    incoming = [tuple(map(int, input().split())) for _ in range(M)]

    cx, cy = 0, 0
    score = 0

    for step in range(M):
        best_idx = -1
        best_d2 = -1

        for i, (x, y) in enumerate(targets):
            d2 = dist2(cx, cy, x, y)
            if d2 > best_d2:
                best_d2 = d2
                best_idx = i
        bx ,by = targets[best_idx]
        score += best_d2
        cx, cy = bx, by

        targets.pop(best_idx)

        if step < M:
            targets.append(incoming[step])
    print(score)

solve()