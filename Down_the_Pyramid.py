import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


INF = 10**30
low = 0
high = INF

s = 1
t = 0

for i in range(N +1):
    if s == 1:
        low = max(low, -t)
    else:
        high = min(high, t)
    
    if i == N:
        break
    
    s = -s
    t = arr[i] - t

print(max(0, high - low + 1))