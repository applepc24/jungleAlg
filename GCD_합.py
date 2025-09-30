import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    n, arr = nums[0], nums[1:]

    total = 0
    for i in range(n):
        for j in range(i+1, n):
            a, b = arr[i], arr[j]
            while b != 0:
                a, b = b, a%b
            total += a
    print(total)
