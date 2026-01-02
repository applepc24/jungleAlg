import sys
input = sys.stdin.readline

N = int(input())
swit = list(map(int, input().split()))
stu = int(input())

def toggle(x):
    swit[x] = 1 - swit[x]

for _ in range(stu):
    sex, k = map(int, input().split())
    k -= 1

    if sex == 1:
        step = k + 1
        i = k
        while i < N:
            toggle(i)
            i += step
    else:
        d = 0
        while k - d >= 0 and k + d < N and swit[k-d] == swit[k+d]:
            d += 1
        d -= 1

        for i in range(k-d, k+d+1):
            toggle(i)

for i in range(N):
    print(swit[i], end = ' ')
    if (i+1) % 20 == 0:
        print()
