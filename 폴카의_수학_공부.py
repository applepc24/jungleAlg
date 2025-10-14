import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    s = input().strip()

    p = s.find('-')
    if p == -1:
        print('YES')
        continue
    tail = s[p+2:]
    ok = True
    for ch in tail:
        if '1' <= ch <= '9':
            ok = False
            break
    print("YES" if ok else 'NO')