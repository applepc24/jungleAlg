import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque(range(1, N+1))
result = []

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<" + ", " .join(map(str, result)) + ">")