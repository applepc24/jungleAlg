n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

#친구 관계
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 친구 관계가 2이상이면 리턴
# 관계가 2이하 이면서 아직 방문이 False 이면
# 방문을 True 바꿔주고 count 1 올리고
# 재귀
def dfs(node, rel):
    global count
    if rel > 2:
        return

    for friend in graph[node]:
        if not visited[friend]:
            visited[friend] = True
            count += 1
            dfs(friend, rel+1)

# 상근이는 무조건 방문처리 그다음 부터 설정
visited[1] =True
dfs(1, 0)
print(count)