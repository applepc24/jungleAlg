import sys
from typing import Any

input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    command = input().split()

    op = command[0]
    if len(command) > 1:
        param = int(command[1])
    else:
        param = None
    arr.append((op, param))

class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front_index = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0
        
    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        return x
    
    def deque(self) -> Any:
        if self.is_empty():
            return -1
        x = self.que[self.front_index]
        self.front_index +=1
        self.no -= 1
        if self.front_index == self.capacity:
            self.front_index = 0
        return x
    
    def front(self) -> Any:
        if self.is_empty():
            return -1
        return self.que[self.front_index]
    
    def back(self) -> Any:
        if self.is_empty():
            return -1
        back_index = self.rear - 1 if self.rear != 0 else self.capacity - 1
        return self.que[back_index]

queue = FixedQueue(N)

for cmd in arr:
    op, param = cmd
    if op == 'push':
        queue.enque(param)
    if op == 'front':
        print(queue.front())
    if op == 'back':
        print(queue.back())
    if op == 'size':
        print(len(queue))
    if op == 'empty':
        print(1 if queue.is_empty() else 0)
    if op == 'pop':
        print(queue.deque())
