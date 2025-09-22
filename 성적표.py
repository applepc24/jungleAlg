import sys

input = sys.stdin.readline
N = int(input())
xs, ys = [], []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


Sx = sum(xs)
Sy = sum(ys)
Sxx = sum(x*x for x in xs)
Sxy = sum(x*y for x, y in zip(xs, ys))
Syy = sum(y*y for y in ys)

best_a = best_b = 1
best_rss = None

for a in range(1, 101):
    a2_Sxx = a*a * Sxx
    minus2a_Sxy = -2*a *Sxy
    for b in range(1,101):
        rss = (
            a2_Sxx
            + 2*a*b*Sx
            + N*(b*b)
            + minus2a_Sxy
            -2*b*Sy
            +Syy
        )
        if best_rss is None or rss < best_rss:
            best_rss = rss
            best_a, best_b = a, b

print(best_a, best_b)