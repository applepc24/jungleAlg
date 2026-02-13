import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
ans = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack[-1] > y:
        h = stack.pop()
        if h != 0:
            ans += 1
    
    if stack[-1] < y:
        stack.append(y)

while stack:
    h = stack.pop()
    if h != 0:
        ans += 1

print(ans)