import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
length = len(bomb)

stack = []

for char in string:
    stack.append(char)

    if len(stack) >= length:
        if ''.join(stack[-length:]) == bomb:
            for _ in range(length):
                stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")