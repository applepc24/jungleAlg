import sys
input = sys.stdin.readline

k = int(input())
g = list(map(int, input().split()))
S = sum(g)

reachable = bytearray(S + 1)

def dfs(i, cur):
    if i == k:
        reachable[abs(cur)] = 1
        return
    
    dfs(i + 1, cur -g[i])
    dfs(i + 1, cur)
    dfs(i + 1, cur + g[i])

dfs(0, 0)

print(S - sum(reachable[1:]))