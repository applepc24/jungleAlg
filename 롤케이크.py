import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A= list(map(int, input().split()))

ans = 0
t = []
nt = []

for L in A:
    if L == 10:
        ans += 1
    elif L % 10 == 0:
        t.append(L)
    else:
        nt.append(L)

t.sort()

for L in t:
    while M >0 and L > 10:
        L -= 10
        ans += 1
        M -= 1
    if L == 10:
        ans += 1
    
for L in nt:
    while M >0 and L > 10:
        L -= 10
        ans += 1
        M -= 1

print(ans)
