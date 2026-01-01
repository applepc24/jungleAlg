import sys
input =sys.stdin.readline

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

arr = []
for i in range(N):
    rank = 1
    wi, li = people[i]
    for j in range(N):
        wj, lj = people[j]
        if i == j:
            continue
        if wj > wi and lj > li:
            rank += 1
    arr.append(rank)
print(*arr)
         

