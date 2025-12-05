import sys
input = sys.stdin.readline

N, K = map(int, input().split())
As, Ae ,Bs, Be, Cs, Ce = map(int, input().split())

DAY = 1440

curL, curR = As, Ae

total_piils = 3 * N

for i in range(1 , total_piils):
    day = i // 3
    meal = i %  3

    base = day * DAY

    if meal == 0:
        S, E = As + base, Ae + base
    elif meal == 1:
        S, E = Bs + base, Be + base
    else:
        S, E = Cs + base, Ce + base
    
    newL = max(S, curL)
    newR = min(E, curR + K)

    if newL > newR:
        print('NO')
        break
    
    curL, curR = newL, newR
else:
    print("YES")



