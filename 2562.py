nums = []

for _ in range(9):
    nums.append(int(input()))

maxNum = nums[0]
maxNumIndex = 0

for i in range(len(nums)):
    if maxNum < nums[i]:
        maxNum = nums[i]
        maxNumIndex = i

print(maxNum)
print(maxNumIndex + 1)
