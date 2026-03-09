import sys
input = sys.stdin.readline
N, L = map(int, input().split())

pools = [tuple(map(int, input().split())) for _ in range(N)]

pools.sort()

cover = 0
answer = 0

for s, e in pools:
    if cover > s:
        s = cover
    
    length = e - s
    cnt = (length + L - 1) // L
    answer += cnt
    cover = s + cnt * L
print(answer)