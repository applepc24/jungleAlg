import sys
input = sys.stdin.readline

N = int(input())

line = []
arr = list(map(int, input().split()))
for i in range(N, 0, -1):
    pos = arr[i-1]
    line.insert(pos, i)
print(*line)
