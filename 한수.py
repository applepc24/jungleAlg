# N = int(input())

# count = 0

# if N <= 99:
#     count = N
# else:
#     count = 99
#     for num in range(100, N+1):
#        spli = list(map(int, str(num)))
#        if spli[1] - spli[0] == spli[2] - spli[1]:
#         count += 1

# print(count)

def hansu(num):
    digits = list(map(int, str(num)))

    if len(digits) < 2:
        return True
    
    diff = digits[1] - digits[0]

    for i in range(1, len(digits)-1):
        if digits[i+1] - digits[i] != diff:
            return False
    return True

N = int(input())
count = 0

for num in range(1, N+1):
    if hansu(num) == True:
        count += 1

print(count)
