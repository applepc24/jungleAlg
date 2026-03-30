import sys
input = sys.stdin.readline
N = int(input())

start = 1
length = 1
answer = 0

while start * 10 <= N:
    answer += (start * 10 - start) * length
    start *= 10
    length += 1

answer += (N - start + 1) * length
print(answer)