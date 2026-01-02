import sys
input = sys.stdin.readline

n, s, p = map(int, input().split())
scores = list(map(int, input().split()))

if n == 0:
    print(1)
    sys.exit(0)

if n == p and scores[-1] >= s:
    print(-1)
else:
    rank = 1
    for x in scores:
        if x > s:
            rank += 1
    print(rank)
