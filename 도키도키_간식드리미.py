import sys
input = sys.stdin.readline

N = int(input())
arr = map(int, input().split())

need = 1
stack = []

for i in arr:
    while stack and stack[-1] == need:
        stack.pop()
        need += 1
    
    if i == need:
        need += 1
    else:
        stack.append(i)

while stack and stack[-1] == need:
    stack.pop()
    need += 1

if need == (N + 1):
    print('Nice')
else:
    print('Sad')