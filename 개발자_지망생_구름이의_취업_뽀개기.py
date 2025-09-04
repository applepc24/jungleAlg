# 인풋 받기
import sys
input = sys.stdin.readline

N = int(input())
Q = list(map(int, input().split()))
buckets = [[] for _ in range(5)]

for _ in range(N):
    k, t = map(int, input().split())
    buckets[k-1].append(t)


# 구간 최소값 구하는 함수 만들기

def min_cost(times, need):
    times.sort()
    m = len(times)

    ps = [0]
    for x in times:
        ps.append(ps[-1] + x)

    best = float('inf')

    for i in range(0, m- need +1):
        j = i+need-1
        seg_sum = ps[j + 1] - ps[i]
        range_cost = times[j] - times[i]
        cost = seg_sum + range_cost

        if cost < best:
            best = cost
    return best

total = 0
for j in range(5):
    total += min_cost(buckets[j], Q[j])
    
total += 60 * 4
print(total)


