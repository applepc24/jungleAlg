import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

l, r = 0, n-1
best_sum = 10 ** 19
bets_pair = (a[l], a[r])

while l < r:
    s = a[l] + a[r]

    if abs(s) < abs(best_sum):
        best_sum = s
        bets_pair = (a[l], a[r])
        if best_sum == 0:
            break
    
    if s < 0:
        l += 1
    else:
        r -= 1

print(bets_pair[0], bets_pair[1])