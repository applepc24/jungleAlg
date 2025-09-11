import sys

input = sys.stdin.readline
N = int(input())
rows = [int(input()) for _ in range(N)]

max_row = max(rows)
free = [0] * (max_row + 2)

answer = 0

for R in rows:
    a= [0] * (R + 2)
    a[1] = max(0, free[1])

    for j in range(2, R + 1):
        a[j] = max(a[j-1]+ 1, free[j])
    
    end_time = a[R] + 5
    answer = max(answer, end_time)

    free[R] = max(free[R], end_time)

    for j in range(R -1, 0, -1):
        free[j] = max(free[j], a[j+1])

print(answer)