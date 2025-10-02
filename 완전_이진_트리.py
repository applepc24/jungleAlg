import sys
input = sys.stdin.readline

K = int(input())
arr = list(map(int, input().split()))

levels = [[] for _ in range(K)]

def solve(l, r, depth):
    if l > r or depth == K:
        return
    mid = (l + r) // 2
    levels[depth].append(arr[mid])

    solve(l, mid -1, depth +1)
    solve(mid +1 , r, depth + 1)

solve(0, len(arr) -1, 0)

for line in levels:
    print(*line)