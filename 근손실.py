import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

used = [False] * N
ans = 0

def dfs(day, w):
    global ans
    if day == N:
        ans += 1
        return
    
    for i in range(N):
        if not used[i]:
            ws = w + A[i] - K
            if ws >= 500:
                used[i] = True
                dfs(day + 1, ws)
                used[i] = False
dfs(0, 500)
print(ans)