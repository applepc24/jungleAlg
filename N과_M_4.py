import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0]*m

def dfs(depth, start):
    if depth == m:
        print(*arr)
        return
    for x in range(start, n+1):
        arr[depth] = x
        dfs(depth+1, x)

dfs(0, 1)