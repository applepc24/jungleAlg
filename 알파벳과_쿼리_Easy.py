import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
s = list(input().strip())

for _ in range(Q):
    t, l , r = map(int, input().split())
    l -= 1
    r -= 1

    if t == 2:
        for i in range(l, r+1):
            if s[i] == 'Z':
                s[i] = 'A'
            else:
                s[i] = chr(ord(s[i]) + 1)
    else:
        cnt = 1
        for i in range(l+1, r+1):
            if s[i] != s[i-1]:
                cnt +=1
        print(cnt)
