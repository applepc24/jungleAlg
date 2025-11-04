import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

T = (9 * M +9) // 10
cnt = {}

for i in range(M):
    v = A[i]
    if v in cnt:
        cnt[v] += 1
    else:
        cnt[v] = 1
    
    if cnt[v] >= T:
        print('YES')
        sys.exit(0)

for i in range(M, N):
    rm = A[i - M]
    cnt[rm] -= 1
    if cnt[rm] == 0:
        del cnt[rm]
    
    v = A[i]
    if v in cnt:
        cnt[v] += 1
    else:
        cnt[v] =1
    
    if cnt[v] >= T:
        print('YES')
        sys.exit(0)
print('NO')
