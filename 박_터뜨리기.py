import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(range(1, K+1))

need = K * (K + 1) // 2

if N < need:
    print(-1)
    sys.exit(0)

E = N - need
i = K -1
while E > 0:
    arr[i] += 1
    E -= 1
    i -= 1
    if i < 0:
        i = K - 1
print(arr[-1] - arr[0])