import sys
input = sys.stdin.readline

while True:
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z ==0:
        break

    side = sorted([x, y, z])

    if (side[0] ** 2) + (side[1] ** 2) == side[2] ** 2:
        print("right")
    else:
        print("wrong")