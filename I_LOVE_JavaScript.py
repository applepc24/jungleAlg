import sys
input =sys.stdin.readline
s = input().strip()

tokens = s.split()

stack = []
result = 0

for tok in tokens:
    if tok == '[':
        stack.append(0)
    elif tok == ']':
        inner_sum = stack.pop()
        obj_size = inner_sum + 8
        if stack:
            stack[-1] += obj_size
        else:
            result = obj_size
    else:
        if tok.isdigit():
            size = 8
        else:
            size = len(tok) + 12
        
        stack[-1] += size
print(result)
