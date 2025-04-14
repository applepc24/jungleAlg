from typing import Any

N = int(input())

arr = []
for _ in range(N):
    command = input().split()

    op = command[0]
    if len(command) > 1:
        param = int(command[1])
    else:
        param = None

    arr.append((op, param))

class FixedStack:    
    def __init__(self, capacity:int = N) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0


    def push(self , Value:Any) -> None:
        self.stk[self.ptr] =Value
        self.ptr += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def top(self) -> Any:
        if self.is_empty():
            return -1
        return self.stk[self.ptr-1]

    def empty(self) -> int:
        if self.is_empty():
            return 1
        else:
            return 0

stack = FixedStack(N)

for cmd in arr:
    op, param = cmd
    if op == 'push':
        stack.push(param)
    elif op == 'pop':
        print(stack.pop())
    elif op == 'size':
        print(stack.__len__())
    elif op == 'empty':
        print(stack.empty())
    elif op == 'top':
        print(stack.top())