numbers = []
for _ in range(3):
    numbers.append(int(input()))

total = 1
for i in numbers:
    total *= i
arr = []
arr.append(list(str(total)))

for i in range(10):
    print(arr[0].count(str(i)))
    
    




