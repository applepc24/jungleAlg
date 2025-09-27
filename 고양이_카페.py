N, K = map(int, input().split())
W = list(map(int, input().split()))

ans = 0
i, j = 0, N -1
W.sort()

while i < j:
    if W[i] + W[j] <= K:
        ans += 1
        i += 1
        j -= 1
    else:
        j -= 1
print(ans)