import sys
input = sys.stdin.readline

N, R = map(int, input().split())
returned = [False] * (N+1)

nums = list(map(int, input().split()))
for x in nums:
    returned[x] = True

lost = []
for i in range(1, N+1):
    if not returned[i]:
        lost.append(i)

if not lost:
    print('*')
else:
    for x in lost:
        print(x, end= " ")
    