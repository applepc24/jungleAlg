n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * (n)
find = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, rel):
    global find
    if rel == 4:
        find = True
        return
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei, rel + 1)
        if find:
            return
    visited[node] = False

for i in range(n):
    dfs(i, 0)
    if find:
        break

print(1 if find else 0)

    


