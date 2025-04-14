import sys

input = sys.stdin.readline

# 입력 받기
N, C = map(int, input().split())  # 집의 개수, 공유기 개수
houses = [int(input()) for _ in range(N)]
houses.sort()  # 반드시 정렬해야 함

low = 1
high = houses[-1] - houses[0]
result = 0

def can_install(distance):
    count = 1
    start = houses[0]

    for i in range(1, N):
        if houses[i] - start >= distance:
            count += 1
            start = houses[i]
    return(count >= C)

while low <= high:
    mid = (low + high) // 2
    if can_install(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)