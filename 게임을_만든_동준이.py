N = int(input())
scores = [int(input()) for _ in range(N)]

ans = 0

for i in range(N-2, -1, -1):
    if scores[i] >= scores[i + 1]:
        new_val = scores[i + 1] -1
        ans += scores[i] - new_val
        scores[i] = new_val

print(ans)