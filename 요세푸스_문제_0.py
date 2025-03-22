from typing import Any

N, K = map(int, input().split())

queue = [i for i in range(1, N+1)]
capacity = len(queue)

front = K-1
result = []

while len(queue) > 0:
    front = front % len(queue)
    result.append(queue.pop(front))
    front += (K-1)
print("<" + ", ".join(map(str, result)) + ">")