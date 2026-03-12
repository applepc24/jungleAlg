import sys
input = sys.stdin.readline

A, B = map(int, input().split())

arr = []
num = 1
while num < 1000:
    for _ in range(num):
        arr.append(num)
    num += 1

print(sum(arr[A-1:B]))