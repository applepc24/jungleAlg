import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
cnt = 0
max_height = 0

for h in reversed(arr):
    if h > max_height:
        cnt += 1
        max_height = h

print(cnt)