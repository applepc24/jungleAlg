import sys
input = sys.stdin.readline

N = int(input())
car_num = list(map(int, input().split()))

cnt = 0
for i in car_num:
    if i == N:
        cnt += 1
print(cnt)