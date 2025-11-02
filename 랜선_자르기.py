import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

low = 1
high = max(lan)
answer = 0

while low <= high:
    mid = (low + high) // 2

    cnt = 0
    for length in lan:
        cnt += length // mid
    
    if cnt >= N:
        answer = mid
        low = mid + 1
    else:
        high = mid -1

print(answer)
