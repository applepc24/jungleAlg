import sys
input = sys.stdin.readline

T = int(input())

def p2017(a):
    if a == 0:
        return 0
    bound = [1, 3, 6, 10 ,15, 21]
    money = [500, 300, 200, 50, 30 ,10]

    for i in range(len(bound)):
        if a <= bound[i]:
            return money[i]
    return 0


def p2018(b):
    if b == 0:
        return 0
    bound = [1, 3, 7, 15, 31]
    money = [512, 256, 128, 64, 32]  # 만원 단위
    for i in range(len(bound)):
        if b <= bound[i]:
            return money[i]
    return 0


for _ in range(T):
    a,b = map(int, input().split())
    p1 = p2017(a)
    p2 = p2018(b)
    total = (p1 + p2) * 10000
    print(total)