import sys
input = sys.stdin.readline
N = int(input())

acc = {}

for _ in range(N):
    x, t, c = map(int, input().split())
    k = x -t
    acc[k] = acc.get(k, 0) + c

print(max(acc.values())if acc else 0)
