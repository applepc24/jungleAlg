import sys
input = sys.stdin.readline

N = int(input())
piller = []
for _ in range(N):
    L, H = map(int, input().split())
    piller.append((L, H))


piller.sort()

maxH = 0
for L, H in piller:
    if H > maxH:
        maxH = H

first = -1
last = -1
for i in range(N):
    if piller[i][1] == maxH:
        if first == -1:
            first = i
        last = i

area = 0 

curH = 0
for i in range(0, first):
    if piller[i][1] > curH:
        curH = piller[i][1]
    area += curH * (piller[i+1][0] - piller[i][0])

curH = 0
for i in range(N-1, last, -1):
    if piller[i][1] > curH:
        curH = piller[i][1]
    area += curH * (piller[i][0] - piller[i-1][0])

left_maxL = piller[first][0]
right_maxR = piller[last][0]

area += (maxH * (right_maxR - left_maxL + 1))
print(area)
