import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited = [False] * (n+1)
max_distance = 0

def dfs(node, dist):
    global max_distance
    if dist > max_distance:
        max_distance = dist
    visited[node] = True

    for next_node, weight in graph[node]:
        if not visited[next_node]:
            dfs(next_node, dist+weight)

dfs(1,0)
print(max_distance)

