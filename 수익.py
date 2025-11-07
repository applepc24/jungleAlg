import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    
    best = -10**18
    current = 0

    for _ in range(N):
        x= int(input())
        if current + x < x:
            current = x
        else:
            current = current + x
        
        if current > best:
            best = current
    print(best)