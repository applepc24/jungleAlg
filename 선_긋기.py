import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()

low, high = arr[0]
cnt = 0

for i in range(1, len(arr)):
    a, b = arr[i]

    if a > high:
        cnt += high - low
        low, high = a, b
    else:
        if b > high:
            high = b

cnt += high - low
print(cnt)