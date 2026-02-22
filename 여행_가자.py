import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

parent = list(range(N+1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        if row[j-1] == 1:
            union(i, j)

plan = list(map(int, input().split()))
root = find(plan[0])

for city in plan[1:]:
    if find(city) != root:
        print("NO")
        break
else:
    print("YES")