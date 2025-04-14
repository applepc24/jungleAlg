import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()

    arranged = [0] * n
    left, right = 0, n-1

    for i in range(n):
        if i % 2 == 0:
            arranged[left] = trees[i]
            left += 1
        else:
            arranged[right] = trees[i]
            right -= 1
    
    max_diff = 0
    for i in range(n):
        diff = abs(arranged[(i+1) % n] - arranged[i])
        max_diff = max(max_diff, diff)
        
    print(max_diff) 


