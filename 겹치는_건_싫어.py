import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * 100001
l = 0
best = 0

for r in range(n):
    cnt[arr[r]] +=1

    while cnt[arr[r]] > k:
        cnt[arr[l]] -= 1
        l += 1
    best = max(best, r - l + 1)

print(best)

