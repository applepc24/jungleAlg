import heapq, sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

heapq.heapify(arr)

result = 0

while len(arr) > 1:
    one = heapq.heappop(arr)
    two = heapq.heappop(arr)

    temp = one + two
    result += temp
    heapq.heappush(arr, temp)

print(result)

import sys
import heapq

input = sys.stdin.readline

n = int(input())
classes = [tuple(map(int, input().split())) for _ in range(n)]

# 시작 시간 기준 정렬
classes.sort()

# 힙: 현재 진행 중인 수업들의 종료 시간
heap = []

for start, end in classes:
    if heap and heap[0] <= start:
        # 가장 빨리 끝나는 수업이 끝났으면 그 강의실 재사용
        heapq.heappop(heap)
    # 새 수업의 종료 시간 넣기 (새 강의실이든 재사용이든)
    heapq.heappush(heap, end)

# heap 안에 있는 수가 강의실 개수
print(len(heap))