import sys
from collections import deque
input = sys.stdin.readline

def is_bipartite(graph, V):
    color = [-1] * (V+1)

    for start in range(1, V+1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1-color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
    return True

T = int(input())

for _ in range(T):
    V,E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    print("YES" if is_bipartite(graph,V) else "NO")



