import sys
input = sys.stdin.readline

N, M = map(int, input().split())

path = []
out = []

def dfs(start):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return
    for num in range(start , N + 1):
        path.append(num)
        dfs(num + 1)
        path.pop()

dfs(1)
print('\n'.join(out))