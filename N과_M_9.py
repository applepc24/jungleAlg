import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * N
arr= sorted(map(int, input().split()))
path = []


def dfs():
    if len(path) == M:
        print(*path)
        return
    
    prev = None
    for i in range(N):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            path.append(arr[i])
            prev = arr[i]

            dfs()

            path.pop()
            visited[i] = False
dfs()