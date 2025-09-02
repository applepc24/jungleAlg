import sys
input = sys.stdin.readline
 
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
 
if N % 2:
    K = (N // 2) + 1
else:
    K = N // 2
 
result = 0
for i in range(K):
    num = numbers[i]
    while num > 1:
        num = num // 2
        result += 1
 
print(result + 1)