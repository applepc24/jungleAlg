import sys

for line in sys.stdin:
    N, M = map(int, line.split())

    cnt = 0
    for x in range(N, M + 1):
        s = str(x)
        if len(set(s)) == len(s):
            cnt += 1
    print(cnt)