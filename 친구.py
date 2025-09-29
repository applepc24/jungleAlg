import sys
input = sys.stdin.readline
n = int(input())
A = [input().strip() for _ in range(n)]

ans = 0
for i in range(n):
    seen = [False] *n
    for j in range(n):
        if  i == j:
            continue
        if A[i][j] == 'Y':
            seen[j] = True
        else:
            for k in range(n):
                if A[i][k] == 'Y' and A[k][j] == 'Y':
                    seen[j] = True
                    break
    ans = max(ans, sum(seen))

print(ans)