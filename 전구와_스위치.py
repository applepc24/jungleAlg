import sys
input = sys.stdin.readline

def solve_case(arr, target, press_first):
    n = len(arr)
    a = arr[:]
    cnt = 0

    def press(i):
        nonlocal cnt
        cnt += 1
        for j in (i-1, i, i+1):
            if 0 <= j < n:
                a[j] = 1 - a[j]
    
    if press_first:
        press(0)
    
    for i in range(1, n):
        if a[i-1] != target[i-1]:
            press(i)
    
    return cnt if a == target else None

N = int(input())
cur = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

ans1 = solve_case(cur, goal, press_first=False)
ans2 = solve_case(cur, goal, press_first=True)

cand = []
for x in (ans1, ans2):
    if x is not None:
        cand.append(x)

if cand:
    print(min(cand))
else:
    print(-1)