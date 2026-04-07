import sys
from collections import deque
input = sys.stdin.readline

S = int(input())

MAX = 1001
dist = [[-1] * MAX for _ in range(MAX)]

q = deque([(1,0)])
dist[1][0] = 0

while q:
    screen, clip = q.popleft()

    if screen == S:
        print(dist[screen][clip])
        break

    if dist[screen][screen] == -1:
        dist[screen][screen] = dist[screen][clip] + 1
        q.append((screen, screen))
        
    if clip > 0 and screen + clip < MAX:
        if dist[screen+clip][clip] == -1:
            dist[screen+clip][clip] = dist[screen][clip] + 1
            q.append((screen+clip, clip))
    
    if screen > 0:
        if dist[screen - 1][clip] == -1:
            dist[screen - 1][clip] = dist[screen][clip] + 1
            q.append((screen - 1, clip))

