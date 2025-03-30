import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

left = 0
right = N -1
min_val = float('inf')
result = (0, 0)

while left < right:
    total = nums[left] + nums[right]
    if abs(total) < min_val:
        min_val = abs(total)
        result = (nums[left], nums[right])

    if total < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
