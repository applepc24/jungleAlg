import sys
input = sys.stdin.readline

n = int(input())
a = [0] + [int(input()) for _ in range(n)]

visited = [False] * (n+1)
in_stack = [False] * (n+1)
ans = []

def dfs(start):
    path = []
    cur = start

    while True:
        visited[cur] = True
        in_stack[cur] = True
        path.append(cur)

        nxt = a[cur]

        if not visited[nxt]:
            cur = nxt
            continue

        if in_stack[nxt]:
            idx = path.index(nxt)
            ans.extend(path[idx:])
        
        for v in path:
            in_stack[v] = False
        return

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

ans = sorted(ans)
print(len(ans))
for x in ans:
    print(x)