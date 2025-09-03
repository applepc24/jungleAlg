import sys

P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

count = 0

for a in A:
    if P >= 200:
        break
    
    P += a
    count +=1

print(count)