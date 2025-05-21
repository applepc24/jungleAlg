# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k = map(int, input().split())
# stone = list(map(int, input().split()))

# reached = [0 for _ in range(n)]

# q = deque([0])
# reached[0] =1

# while q:
#     a = q.popleft()
#     for b in range(a+1, n):
#         if(b-a) * (1 +abs(stone[a]- stone[b])) <= k and not reached[b]:
#             reached[b] = 1
#             q.append(b)
#             if b == n-1:
#                 print('YES')
#                 sys.exit(0)

# print('NO')

n, k = map(int, input().split())
stone = list(map(int, input().split()))

dp = [False] * n
dp[0] = True

for i in range(n):
    if not dp[i]:
        continue
    for j in range(i+1 , n):
        cost= (j-i) * (1 + abs(stone[i]-stone[j]))
        if cost <= k:
            dp[j] = True

if dp[n-1]:
    print("YES")
else:
    print("NO")
