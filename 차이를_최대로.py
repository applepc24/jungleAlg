import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

visited = [False] * N
perm = [0] * N
ans = 0
def dfs(depth):
    global ans
    if depth == N:
        s = 0
        for i in range(N-1):
            s += abs(perm[i] - perm[i+1])
            if s > ans:
                ans = s
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            perm[depth] = arr[i]
            dfs(depth + 1)
            visited[i] = False

dfs(0)
print(ans)