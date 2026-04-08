import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dirs = ([(1,0), (-1,0), (0,1), (0,-1)])

def fire_bfs(fire_q, board, fire_visited, w, h):
    while fire_q:
        x, y = fire_q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] != '#' and fire_visited[ny][nx] == -1:
                    fire_visited[ny][nx] = fire_visited[y][x] + 1
                    fire_q.append((nx,ny))

def sg_bfs(sg_q, board, sg_visited, fire_visited,w, h):
    while sg_q:
        x, y = sg_q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            next_time = sg_visited[y][x] + 1

            if not (0 <= nx < w and 0 <= ny < h):
                return next_time
            
            if board[ny][nx] == '#':
                continue

            if sg_visited[ny][nx] != -1:
                continue
            
            if fire_visited[ny][nx] != -1 and fire_visited[ny][nx] <= next_time:
                continue

            sg_visited[ny][nx] = next_time
            sg_q.append((nx, ny))
    return "IMPOSSIBLE"


for _ in range(T):
    w, h = map(int, input().split())
    
    board = [list(input().strip()) for _ in range(h)]
    fire_visited = [[-1] * w for _ in range(h)]
    sg_visited = [[-1] * w for _ in range(h)]

    fire_q = deque()
    sg_q = deque()

    for y in range(h):
        for x in range(w):
            if board[y][x] == '*':
                fire_q.append((x,y))
                fire_visited[y][x] = 0
            if board[y][x] == '@':
                sg_q.append((x,y))
                sg_visited[y][x] = 0
    fire_bfs(fire_q, board, fire_visited, w, h)

    ans = sg_bfs(sg_q, board, sg_visited, fire_visited,w, h)
    print(ans)