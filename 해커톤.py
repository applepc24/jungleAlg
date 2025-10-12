import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

X.sort()

team = 0
cnt = 0
need = None

for x in X:
    if cnt == 0:
        need = x
    cnt += 1
    if need == cnt:
        team += 1
        cnt = 0
if cnt > 0:
    team += 1
print(team)

