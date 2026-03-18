import sys
input = sys.stdin.readline

a1 = int(input().strip())
a2 = int(input().strip())
a3 = int(input().strip())
a4 = int(input().strip())
a5 = int(input().strip()) 
a6 = int(input().strip())

ans = 0

ans += a6
ans += a5
a1 = max(0, a1 - 11 * a5)

ans += a4
need2 = 5 * a4
if a2 >= need2:
    a2 -= need2
else:
    lack2 = need2 - a2
    a2 = 0
    a1 = max(0, a1 - lack2 * 4)

ans += a3 // 4
rem3 = a3 % 4

if rem3:
    ans += 1
    if rem3 == 1:
        if a2 >= 5:
            a2 -= 5
            a1 = max(0, a1 - 7)
        else:
            lack2 = 5 - a2
            a2 = 0
            a1 = max(0, a1-(7+lack2 * 4))
    elif rem3 == 2:
        if a2 >= 3:
            a2 -= 3
            a1 = max(0, a1 - 6)
        else:
            lack2 = 3 - a2
            a2 = 0
            a1 = max(0, a1 - (6+ lack2 * 4))
    else:
        if a2 >= 1:
            a2 -= 1
            a1 = max(0, a1 - 5)
        else:
            a1 = max(0, a1 - 9)

ans += a2 // 9
rem2 = a2 % 9

if rem2:
    ans += 1
    a1 = max(0, a1 - (36 - rem2 * 4))

ans += (a1 + 35) // 36
print(ans)
