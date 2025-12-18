import sys
input = sys.stdin.readline

N = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(N)]

rooms.sort(key = lambda x: (x[1], x[0]))

cnt = 0
last_end = 0

for start, end in rooms:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)