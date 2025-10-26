import sys
input = sys.stdin.readline
N, K = map(int, input().split())
tem = list(map(int, input().split()))

window_sum = sum(tem[0:K])
max_sum = window_sum

for start in range(1, N-K+1):
    window_sum += tem[start +K -1]
    window_sum -= tem[start - 1]

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)
