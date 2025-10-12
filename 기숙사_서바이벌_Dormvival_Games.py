import sys
input = sys.stdin.readline

N, A, B, M = map(int, input().split())

rooms = list(range(1, N+1))
pos = list(range(N+1))

for i, stu in enumerate(rooms):
    pos[stu] = i

def happy():
    return abs(pos[1] - pos[A]) <= B

happy_cnt = 0
cur_stack = 0
best_stack = 0
if happy():
    happy_cnt += 1
    cur_stack += 1
    best_stack = max(best_stack, cur_stack)
else:
    cur_stack = 0

for _ in range(M-1):
    awards = list(map(int, input().split()))
    pens = list(map(int, input().split()))

    s = [0] * (N + 1)
    for stu in range(1, N+1):
        s[stu] = awards[stu -1] - pens[stu -1]

    for g in range(N-1):
            u = rooms[g]
            v = rooms[g + 1]

            su, sv = s[u], s[v]

            swap = False
            if su >= 0 and sv >= 0:
                if sv - su >= 2:
                    swap = True
            elif su >= 0 and sv < 0:
                swap = False
            elif su < 0 and sv >= 0:
                swap = True
            else:
                if sv - su >= 4:
                    swap = True
            
            if swap:
                rooms[g], rooms[g + 1] = rooms[g+1], rooms[g]
                pos[u], pos[v] = pos[v], pos[u]

                s[v] -= 2
                s[u] += 2
        
    if happy():
            happy_cnt += 1
            cur_stack += 1
            best_stack = max(best_stack, cur_stack)
    else:
        cur_stack = 0

print(happy_cnt, best_stack)