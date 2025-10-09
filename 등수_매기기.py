import sys
input = sys.stdin.readline

N = int(input())
rank = [int(input()) for _ in range(N)]

rank.sort()
ans = 0
for i, a in enumerate(rank, start = 1):
    ans += abs(i-a)

print(ans)