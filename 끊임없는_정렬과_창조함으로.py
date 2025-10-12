import sys
input = sys.stdin.readline

Q = int(input())

arr = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[1] == 1:
            arr.sort()
        else:
            arr.sort(reverse= True)
    else:
        _, x, t = query
        arr.insert(x, t)

print(len(arr))
if arr:
    print(*arr)
