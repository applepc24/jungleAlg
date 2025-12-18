import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

cnt = 0
ans = 0
i = 1
while i < M -1:
    if S[i-1] == 'I' and S[i]=='O' and S[i+1] == 'I':
        cnt += 1
        if cnt >= N:
            ans +=1
        i += 2
    else:
        cnt = 0
        i += 1

print(ans)
