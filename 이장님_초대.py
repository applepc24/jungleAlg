import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))

t.sort(reverse = True)

ans = 0
for i in range(N):
    n = t[i] + i + 2
    ans = max(n, ans)

print(ans)