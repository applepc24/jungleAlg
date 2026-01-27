import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w

mx = 0
for i in range(w):
    if a[i] > mx:
        mx = a[i]
    left_max[i] = mx

mx= 0
for i in range(w - 1, -1, -1):
    if a[i] > mx:
        mx = a[i]
    right_max[i] = mx

ans = 0
for i in range(w):
    water = min(left_max[i], right_max[i]) - a[i]
    if water > 0:
        ans += water

print(ans)