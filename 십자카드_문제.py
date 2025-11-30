import sys
input = sys.stdin.readline
a,b,c,d = map(int, input().split())

def clock_num(a,b,c,d):
    nums=[
        a*1000 + b*100 + c*10 + d,
        b*1000 + c*100 + d*10 + a,
        c*1000 + d*100 + a*10 + b,
        d*1000 + a*100 + b*10 + c,
    ]
    return min(nums)

my_clock = clock_num(a,b,c,d)

cnt = 0
for x in range(1111, my_clock + 1):
    A = x // 1000
    B = (x // 100) % 10
    C = (x // 10) % 10
    D = x % 10


    if 0 in (A,B,C,D):
        continue
    if clock_num(A,B,C,D) == x:
        cnt += 1

print(cnt)


