import sys
import math

def is_prime(x):
    prime = [True] * (x+1)
    prime[0] = prime[1] = False

    for i in range(2, int(math.sqrt(x))+1):
        if prime[i]:
            for j in range(i*i, x+1, i):
                prime[j] = False
    return prime

numbers = []
T= int(input())
for _ in range(T):
    numbers.append(int(input()))

max_n = max(numbers)
prime = is_prime(max_n)

for n in numbers:
    a = n//2
    b = n//2
    
    while a > 1:
        if prime[a] and prime[b]:
            print(f"{a} {b}")
            break
        a -= 1
        b += 1
