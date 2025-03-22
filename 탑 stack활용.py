from typing import Any


N = int(input())
heights = list(map(int, input().split()))

class FixedStack:

    class Empty(Exception):
        pass

    def __init__(self, capacity: int = N ) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def push(self, value : Any) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise.FixedStack.Empty()
        self.ptr -= 1
        return self.stk[self.ptr]
    def peek(self) -> Any:
        if self.is_empty():
            rasie.FixedStack.Empty()
        return self.stk[self.ptr -1]


result = [0] * N
stack_arr = []
stack = FixedStack(N)

while True:
    if not stack.is_empty():
        break
    if stack.peek(0)


stack.push()