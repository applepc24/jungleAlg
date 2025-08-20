from collections import deque

A, B = map(int, input().split())

queue = deque()
queue.append((A, 1))

found = False
while queue:
    curr, count = queue.popleft()

    if curr == B:
        print(count)
        found = True
        break
    
    if curr * 2 <= B:
        queue.append((curr * 2, count +1))
    if curr * 10 + 1 <= B:
        queue.append((curr * 10 + 1, count + 1))

if not found:
    print(-1)