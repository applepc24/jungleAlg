import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()
A = []
B = []

for _ in range(N):
    data = input().split()

    if data[0] == '1':
        a = int(data[1])
        b = int(data[2])
        queue.append((a,b))

    else:
        b = int(data[1])
        stu_id, fav = queue.popleft()

        if fav == b:
            A.append(stu_id)
        else:
            B.append(stu_id)

C = []
for stu_id, fav in queue:
    C.append(stu_id)

A.sort()
B.sort()
C.sort()

def print_list(lst):
    if not lst:
        print('None')
    else:
        print(" ".join(map(str, lst)))

print_list(A)
print_list(B)
print_list(C)
