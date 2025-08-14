import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
k = float(input())

for i in range(n):
    diff1 = A[i] - k * (i + 1)

    if diff1 == 0:
        print("T")
        break
    
    if i < n-1:
        diff2 = A[i+1] - k * (i + 2)
        if diff1 * diff2 < 0:
            print("T")
            break
else:
    print("F")