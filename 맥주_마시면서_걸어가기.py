import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())

    places = []
    for _ in range(n+2):
        x,y = map(int, input().split())
        places.append((x,y))

    visited = [False] * (n+2)
    q = deque([0])
    visited[0] = True

    while q:
        cur = q.popleft()
        if cur == n+1:
            print("happy")
            break

        for nxt in range(1, n+2):
            if not visited[nxt]:
                x1, y1 = places[cur]
                x2, y2 = places[nxt]

                dist = abs(x1 - x2) + abs(y1 - y2)
                if dist <= 1000:
                    visited[nxt] = True
                    q.append(nxt)
    else:
        print("sad")