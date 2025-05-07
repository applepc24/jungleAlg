n = int(input())
arr = list(map(int, input().split()))
ai = int(input()) -1
visited = [False] * n

def dfs(x):
    visited[x] = True
    next_right = x + arr[x]
    if 0 <= next_right < n and not visited[next_right]:
        dfs(next_right)
    next_left = x - arr[x]
    if 0 <= next_left < n and not visited[next_left]:
        dfs(next_left)

dfs(ai)

print(sum(visited))


