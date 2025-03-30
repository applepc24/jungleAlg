import sys
input = sys.stdin.readline

N , C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

low = 1
high = houses[-1] -houses[0]
result = 0

def install(distance):
    count = 1
    start = houses[0]

    for i in range(1, N):
        if houses[i] - start >= distance:
            count += 1
            start = houses[i]
    return (count >= C)

while low <= high:
    mid = (low + high) // 2
    if install(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)



