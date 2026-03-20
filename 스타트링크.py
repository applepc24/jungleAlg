import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())

visited = [-1] * (f+1)
q = deque([s])
visited[s] = 0

while q:
    cur = q.popleft()
    if cur == g:
        print(visited[cur])
        break
    
    up = cur + u
    down = cur - d

    if up <= f and visited[up] == -1:
        visited[up] = visited[cur] + 1
        q.append(up)
    
    if down >= 1 and visited[down] == -1:
        visited[down] = visited[cur] + 1
        q.append(down)
else:
    print("use the stairs")