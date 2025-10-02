import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
tops = [int(input().strip()) for _ in range(N)]

tops.sort(reverse = True)

cal_SUM = C
cost_SUM = A

for d in tops:
    if d * cost_SUM > B * cal_SUM:
        cal_SUM += d
        cost_SUM += B
    else:
        break

print(cal_SUM // cost_SUM)