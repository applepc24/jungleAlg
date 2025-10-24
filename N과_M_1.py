import sys


n, m = map(int, input().split())

used = [False] * (n + 1)
path = [0] * m
out_lines = []


def dfs(depth):
    if depth == m:
        out_lines.append(" ".join(map(str, path)))
        return
    for x in range(1, n + 1):
        if not used[x]:
            used[x] = True
            path[depth] = x
            dfs(depth + 1)
            used[x] = False

dfs(0)
print("\n".join(out_lines))


