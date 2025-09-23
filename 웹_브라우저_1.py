import sys
input = sys.stdin.readline

N, Q, C = map(int, input().split())
CAP = [0] + list(map(int, input().split()))

back = []
forward = []
cur = None
used = 0

def clear_forward():
    global forward, used
    if forward:
        used_sub = sum(CAP[p] for p in forward)
        used -= used_sub
        forward.clear()


def evict_from_back_until_fit():
    global back, used
    while used > C:
        oldest = back.pop(0)
        used -= CAP[oldest]

def compress_back():
    global back, used
    if not back:
        return
    
    removed_sum = 0
    new_top2bottom = []
    last = None
    for i in range(len(back) - 1, -1, -1):
        p = back[i]
        if p == last:
            removed_sum += CAP[p]
        else:
            new_top2bottom.append(p)
            last = p
    
    back = list(reversed(new_top2bottom))
    used -= removed_sum

for _ in range(Q):
    line = input().split()
    op = line[0]

    if op == 'B':
        if back:
            if cur is not None:
                forward.append(cur)
            cur = back.pop()
    elif op == 'F':
        if forward:
            if cur is not None:
                back.append(cur)
            cur = forward.pop()
    elif op == 'A':
        p = int(line[1])
        clear_forward()
        if cur is not None:
            back.append(cur)
        cur = p
        used += CAP[p]

        evict_from_back_until_fit()
    elif op == 'C':
        compress_back()

print(cur)

if back:
    print(*reversed(back))
else:
    print(-1)

if forward:
    print(*reversed(forward))
else:
    print(-1)
