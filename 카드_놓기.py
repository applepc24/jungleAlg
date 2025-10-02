import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

cards = [input().strip() for _ in range(n)]

seen = set()
visited = [False] * n

def dfs(depth, built):
    for i in range(n):
        if depth == k:
            seen.add(built)
            return
        
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, built + str(cards[i]))
            visited[i] = False

dfs(0, "")

print(len(seen))