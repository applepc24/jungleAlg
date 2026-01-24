import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

S = input().strip()
T = input().strip()

memo = {}

def dfs(t):
    if len(t) == len(S):
        return t == S
    
    if t in memo:
        return memo[t]
    
    if t[-1] == 'A':
        if dfs(t[:-1]):
            memo[t] = True
            return True
    
    if t[0] == 'B':
        if dfs(t[1:][::-1]):
            memo[t] = True
            return True
    
    memo[t] = False
    return False

if dfs(T):
    print(1)
else:
    print(0)