import sys
input = sys.stdin.readline

holsu = []
for _ in range(7):
    N = int(input())
    if N % 2 == 1:
        holsu.append(N)

if len(holsu) == 0:
    print(-1)
else:
    print(sum(holsu))
    print(min(holsu))

