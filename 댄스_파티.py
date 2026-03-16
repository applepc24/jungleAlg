import sys
input = sys.stdin.readline

n = int(input())

men = list(map(int, input().split()))
women = list(map(int, input().split()))

m_big = []
m_small = []
w_big = []
w_small = []

for x in men:
    if x > 0:
        m_big.append(x)
    else:
        m_small.append(-x)

for x in women:
    if x > 0:
        w_big.append(x)
    else:
        w_small.append(-x)

m_big.sort()
m_small.sort()
w_big.sort()
w_small.sort()

def women_big(a, b):
    i = j = 0
    cnt = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            j += 1
    return cnt

def men_big(a, b):
    i = j = 0
    cnt = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    return cnt

ans = women_big(m_big, w_small) + men_big(m_small, w_big)
print(ans)
