import sys
input = sys.stdin.readline

N = int(input())
board = [input().strip() for _ in range(N)]

target = "MOBIS"
count = 0

dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

for y in range(N):
    for x in range(N):
        for dy, dx in dirs:
            found = True
            for k in range(5):
                ny = y + dy * k
                nx = x + dx * k
                if not (0 <= ny < N and 0<= nx < N):
                    found = False
                    break
                if board[ny][nx] != target[k]:
                    found = False
                    break
            if found:
                count += 1

print(count)