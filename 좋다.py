import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

cnt = 0

for i in range(N):
    target = A[i]
    l, r = 0, N-1

    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        s = A[l] + A[r]

        if s == target:
            cnt += 1
            break
        elif s < target:
            l += 1
        elif s > target:
            r -= 1
    
print(cnt)