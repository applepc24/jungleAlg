N = int(input())

out = []
path = []

visited = [False] * (N+1)
def dfs():
    if len(path) == N:
        out.append(" ".join(map(str, path)))
        return
    for t in range(1, N + 1):
        if not visited[t]:
            visited[t] = True
            path.append(t)
            dfs()
            path.pop()
            visited[t] = False

dfs()
print("\n".join(out))
        