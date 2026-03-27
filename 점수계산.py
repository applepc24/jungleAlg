import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

score = 0
streak = 0

for i in range(N):
    if arr[i] == 1:
        streak += 1
        score += streak
    else:
        streak = 0

print(score)
