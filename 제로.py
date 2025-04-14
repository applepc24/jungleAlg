from typing import Any

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))


class FixedStack:
    def __init__(self, capacity : int = N) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, Value:int) -> None:
        self.stk[self.ptr] = Value
        self.ptr += 1
    
    def pop(self):
        if self.ptr == 0:
            return 0
        self.ptr -= 1
        return self.stk[self.ptr]

stack = FixedStack(N)

for value in arr:
    if value == 0:
        stack.pop()
    else:
        stack.push(value)
print(sum(stack.stk[:stack.ptr]))
