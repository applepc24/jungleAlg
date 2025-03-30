import bisect
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lis = []

for num in nums:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))

