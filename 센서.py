import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
pos = list(map(int, input().split()))

pos.sort()

if K >= N:
    print(0)
    sys.exit(0)

gaps = []
for i in range(1, N):
    gaps.append(pos[i] - pos[i-1])

gaps.sort(reverse=True)
answer = sum(gaps) - sum(gaps[:K-1])

print(answer)