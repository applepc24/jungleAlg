import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a,w))


def dfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0

    stack = [start]
    while stack:
        cur = stack.pop()

        for nxt, w in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + w
                stack.append(nxt)

    max_dist = 0
    far_node = start
    for i in range(1, n+1):
        if max_dist < visited[i]:
            max_dist = visited[i]
            far_node = i
    
    return far_node, max_dist

far_node, _ = dfs(1)
_, max_dist = dfs(far_node)

print(max_dist)