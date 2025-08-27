def solve(A, B):
    n, m = len(A), len(B)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                curr[j] = prev[j - 1] + 1
                max_len = max(max_len, curr[j])
            else:
                curr[j] = 0  # 이어지지 않으면 초기화
        prev, curr = curr, prev  # swap to reuse memory

    return max_len

A = input().strip()
B = input().strip()
print(solve(A, B))


import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
n, m = len(A), len(B)

prev = [0] * (m + 1)
ans = 0

for i in range(1, n + 1):
    cur = [0] * (m + 1)
    for j in range(1, m + 1):
        if A[i-1] == B[j-1]:
            cur[j] = prev[j-1] + 1
            ans = max(ans, cur[j])
    prev = cur

print(ans)