import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
l = 0
ans = 0
cnt = [0] * 100001

for r in range(n):
    cnt[arr[r]] += 1

    while cnt[arr[r]] > 1:
        cnt[arr[l]] -= 1
        l += 1
    ans += r - l + 1

print(ans)