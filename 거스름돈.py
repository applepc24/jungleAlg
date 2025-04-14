import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n >= 0:
    if n % 5 == 0:
        count = count + n // 5
        print(count)
        break
    n = n - 2
    count += 1
else:
    print(-1)
