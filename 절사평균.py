import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())

S = []
for _ in range(N):
    num = float(input())
    S.append(num)

S.sort()

def julsa(arr ,K):
    mid = (arr[K:len(arr)-K])
    avg = sum(mid) / len(mid)
    avg = math.floor(avg * 100 + 0.5) / 100.0
    return avg 

def bojung(arr, K):
    left, right = arr[K], arr[-K-1]
    W = arr[:]
    for i in range(K):
        W[i] = left
        W[-1-i] = right
    avg = sum(W) / len(W)
    avg = math.floor(avg*100 + 0.5) / 100.0
    return avg

trimmed = julsa(S, K)
winsor  = bojung(S, K)

print(f"{trimmed:.2f}")
print(f"{winsor:.2f}")




