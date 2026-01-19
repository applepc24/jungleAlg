import sys
input = sys.stdin.readline
n = int(input())
s = input().strip()
cntR = s.count('R')
cntB = len(s) - cntR

leftB = 0
while leftB < n and s[leftB] == 'B':
    leftB += 1

leftR = 0
while leftR < n and s[leftR] == "R":
    leftR += 1

rightB = 0
i = n - 1
while i >= 0 and s[i] == 'B':
    rightB += 1
    i -= 1

rightR = 0
i = n - 1
while i >= 0 and s[i] == 'R':
    rightR += 1
    i -= 1

ans = min(cntR - rightR, cntR -leftR, cntB - rightB, cntB - leftB)
print(ans)