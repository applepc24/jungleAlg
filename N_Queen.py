import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

ans = 0
col = set()
diag1 = set()
diag2 = set()

def dfs(r):
    global ans
    if r == n:
        ans += 1
        return

    c= 0
    while c < n:
        if c in col:
            c += 1
            continue
        if (r+c) in diag1:
            c += 1
            continue
        if (r-c)in diag2:
            c += 1
            continue
        
        col.add(c)
        diag1.add(r+c)
        diag2.add(r-c)

        dfs(r+1)

        col.remove(c)
        diag1.remove(r+c)
        diag2.remove(r-c)

        c += 1

dfs(0)
print(ans)