import sys
input = sys.stdin.readline

N, M = map(int, input().split())
needs = []

for _ in range(N):
    P, L = map(int, input().split())
    A = list(map(int, input().split()))

    if P < L:
        needs.append(1)
    else:
        A.sort(reverse=True)
        needs.append(A[L-1])
    
needs.sort()

cnt = 0
spent = 0
for x in needs:
    if spent + x <= M:
        spent += x
        cnt += 1
    else:
        break
print(cnt)