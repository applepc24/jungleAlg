import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
mask = 0
ALL = (1 << 21) -2
out = []

def add(x:int):
    global mask
    mask |= (1 << x)

def remove(x:int):
    global mask
    mask &= ~(1 << x)

def check(x:int):
    write('1\n' if (mask & (1 << x)) else '0\n')

def toggle(x:int):
    global mask
    mask ^= (1 << x)

def all_set():
    global mask
    mask = ALL

def empty():
    global mask
    mask = 0

for _ in range(N):
    parts = input().split()
    op = parts[0]

    if op == "add":
        add(int(parts[1]))
    elif op == "remove":
        remove(int(parts[1]))
    elif op == "check":
        check(int(parts[1]))
    elif op == "toggle":
        toggle(int(parts[1]))
    elif op == "all":
        all_set()
    else:  # empty
        empty()