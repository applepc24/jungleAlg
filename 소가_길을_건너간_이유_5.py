import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = [0] * (N + 1)
for _ in range(B):
    broken[int(input())] = 1

cur = sum(broken[1:K+1])
ans = cur

for i in range(2, N - K + 2):
    r= i + K -1
    cur += broken[r] -broken[i-1]
    if cur < ans:
        ans = cur

print(ans)
    