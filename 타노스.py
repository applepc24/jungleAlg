import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

cnt0 = s.count(str(0))
cnt1 = len(s) - cnt0

tanos0 = cnt0 // 2
tanos1 = cnt1 // 2

tanosed = [False] * n
for i in range(n):
    if tanos1 == 0:
        break
    if s[i] == '1':
        tanosed[i] = True
        tanos1 -= 1

for i in range(n-1, -1, -1):
    if tanos0 == 0:
        break
    if s[i] == '0' and not tanosed[i]:
        tanosed[i] = True
        tanos0 -= 1

ans = []
for i in range(n):
    if tanosed[i] == True:
        continue
    else:
        ans.append(s[i])

print(''.join(ans))
