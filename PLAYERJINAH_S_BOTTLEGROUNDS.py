import sys
input = sys.stdin.readline

pos = [tuple(map(int, input().split())) for _ in range(3)]
(x1, y1), (x2, y2), (x3, y3) = pos

if (x2 -x1)*(y3-y1) - (y2-y1) * (x3-x1) != 0:
    print('WINNER WINNER CHICKEN DINNER!')
else:
    print("WHERE IS MY CHICKEN?")