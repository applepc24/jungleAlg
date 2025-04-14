from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

for comb in combinations(arr, 7):
    if sum(comb) == 100:
        result = sorted(comb)
        
for num in result:
        print(num)




