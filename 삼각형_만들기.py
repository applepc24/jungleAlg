import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort(reverse=True)

for i in range(N-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        print(arr[i] + arr[i+1] + arr[i+2])
        break
else:
    print(-1)