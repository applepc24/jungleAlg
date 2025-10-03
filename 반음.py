import sys
input = sys.stdin.readline

n = int(input())
steps = [int(input().strip()) for _ in range(n)]

white_set = {0, 2, 4, 5, 7, 9, 11}
idx_white = {0:'C', 2:'D', 4:'E', 5:'F', 7:'G', 9:'A', 11:'B'}

start_list = [0, 2, 4, 5, 7, 9, 11]

pairs = []
for i in start_list:
    cur  = i
    ok = True
    for j in steps:
        cur = (cur + j) % 12
        if cur not in white_set:
            ok = False
            break
    if ok:
        start = idx_white[i]
        end = idx_white[cur]
        pairs.append((start, end))

pairs.sort()

for a, b in pairs:
    print(a, b)
