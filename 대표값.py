import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

avg = sum(nums) // 10

count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1

max_cnt = 0
mode = 0

for num, cnt in count.items():
    if max_cnt < cnt:
        max_cnt = cnt
        mode = num

print(avg)
print(mode)