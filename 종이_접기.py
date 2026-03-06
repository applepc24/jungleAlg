import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def ok(s, l, r):
    if l == r:
        return True
    
    mid = (l + r) // 2

    i = 1
    while mid - i >= l and mid + i <= r:
        if s[mid - i] == s[mid + i]:
            return False
        i += 1
    left_ok = ok(s, l, mid - 1)
    right_ok = ok(s, mid + 1, r)
    return left_ok and right_ok

T = int(input())
for _ in range(T):
    S = input().strip()
    if ok(S, 0, len(S) - 1):
        print('YES')
    else:
        print('NO')