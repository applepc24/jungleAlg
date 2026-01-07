import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = list(input().strip())
ans = 0
for i in range(N):
    if s[i] != 'P':
        continue
    
    left = max(0, i - K)
    right = min(N-1, i+K)

    for j in range(left, right+1):
        if s[j] == 'H':
            s[j] = 'x'
            ans += 1
            break
print(ans)
