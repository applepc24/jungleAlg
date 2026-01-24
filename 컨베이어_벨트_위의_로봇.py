import sys 

input = sys.stdin.readline
n, k = map(int, input().split())

negu = list(map(int, input().split()))
robot = [False] * (n)
step = 0

while True:
    step += 1

    negu = [negu[-1]] + negu[:-1]

    robot = [False] + robot[:-1]
    robot[-1] = False

    for i in range(n-2, -1 , -1):
        if robot[i] and not robot[i+1] and negu[i+1] >0:
            robot[i] = False
            robot[i+1] = True
            negu[i+1] -= 1
    
    robot[-1] = False

    if negu[0] > 0 and not robot[0]:
        robot[0] = True
        negu[0] -= 1
    
    if negu.count(0) >= k:
        print(step)
        break