import math

'''
N = int(input())
numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    if num == 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1


print(count)
'''

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime

# 사용 예시
N = 1000
prime = sieve(N)

# numbers 리스트에서 소수 찾기
numbers = [12, 5, 7, 17]
count = 0
for num in numbers:
    if prime[num]:
        count += 1
print(count)
            
