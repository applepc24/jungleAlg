import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

X.sort()

teams = 0
cnt = 0
need = None

for x in X:
    if cnt == 0:
        need = x
    cnt += 1
    if need == cnt:
        teams += 1
        cnt = 0
if cnt > 0:
    teams+=1
print(teams)