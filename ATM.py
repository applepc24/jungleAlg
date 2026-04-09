import sys
input = sys.stdin.readline

N = int(input())

s = list(map(int, input().split()))
s.sort()

time = 0
ans = 0
for i in range(N):
    time = time + s[i]
    ans += time

print(ans)