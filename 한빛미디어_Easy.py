import sys

input = sys.stdin.readline
N = int(input())
books = list(map(int, input().split()))

books.sort()

i = 0
cnt = 0

while i < N:
    j = i
    while j < N and books[j] < 2 * books[i]:
        j +=1
    cnt += 1
    i= j
print(cnt)