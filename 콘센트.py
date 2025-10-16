import sys, bisect
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse = True)
B.sort(reverse = True)

# 의도 : A->B 콘센트를 k개 썼을때 B가 몇개나 생기는지 빠르게 알기위한 누적합을 만든다.
preA = [0]
for a in A:
    preA.append(preA[-1] + a)

# 의도 : B-> A 콘센트를 t개 썼을때 A가 몇개나 생기는지 빠르게 알기위한 누적합을 만든다.
preB = [0]
for b in B:
    preB.append(preB[-1] + b)

# B->A를 t개 쓰려면 B가 t개 필요
T_max = min(m , preA[-1])
ans = 1

for t in range(T_max + 1):
    k = bisect.bisect_left(preA, t)
    if k <= n and preA[k] >= t:
        val = 1 - k + preB[t]
        if val > ans:
            ans = val
print(ans)