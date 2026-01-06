import sys
input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[0:x])
best = window_sum

l = 0
ans = 1
for r in range(x, n):
    window_sum -= arr[l]
    window_sum += arr[r]
    l += 1

    if window_sum > best:
        ans = 1
        best = window_sum
    elif window_sum == best:
        ans += 1

if best == 0:
    print('SAD')
else:
    print(best)
    print(ans) 
        

