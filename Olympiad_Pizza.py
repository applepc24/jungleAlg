import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
q = deque()

for idx, remain in enumerate(arr):
    q.append((idx, remain))

answer = [0] * N
time = 0

while q:
    idx, remain = q.popleft()

    time += 1
    remain -= 1

    if remain == 0:
        answer[idx] = time
    else:
        q.append((idx, remain))

print(*answer)

