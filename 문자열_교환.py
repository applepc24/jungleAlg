import sys
input = sys.stdin.readline

s = input().strip()

A = s.count('a')
if A == 0 or A == len(s):
    print(0)
    sys.exit()

s2 = s + s
cntb = s[:A].count('b')
best = cntb

for i in range(1, len(s)):
    if s2[i-1] == 'b':
        cntb -= 1
    if s2[i + A -1] == 'b':
        cntb += 1
    best = min(cntb, best)
print(best)