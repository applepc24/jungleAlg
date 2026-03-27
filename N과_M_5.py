import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

visited = [False] * N
path = []

def dfs():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])

            dfs()

            path.pop()
            visited[i] = False
dfs()