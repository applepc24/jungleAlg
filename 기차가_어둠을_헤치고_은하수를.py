import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trains = [[0] * 20 for _ in range(n)]

for _ in range(m):
    cmd = list(map(int, input().split()))
    t = cmd[0]
    if t == 1:
        _, i, x = cmd
        trains[i-1][x-1] = 1
    elif t == 2:
        _, i, x = cmd
        trains[i-1][x-1] = 0
    elif t == 3:
        _, i = cmd
        row = trains[i-1]
        for idx in range(19, 0, -1):
            row[idx] = row[idx - 1]
        row[0] = 0
    else:
        _, i = cmd
        row = trains[i-1]
        for idx in range(19):
            row[idx] = row[idx + 1]
        row[19] = 0
seen = set()
for row in trains:
    seen.add(tuple(row))
print(len(seen))