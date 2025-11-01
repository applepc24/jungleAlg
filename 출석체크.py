import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

sleepy_list = list(map(int, input().split()))
starter_list = list(map(int, input().split()))

queries = [tuple(map(int, input().split())) for _ in range(M)]

MAX_ID = N+2

sleepy = [False] * (MAX_ID + 1)
attend = [False] * (MAX_ID + 1)

for s in sleepy_list:
    sleepy[s] = True

for s in starter_list:
    if sleepy[s]:
        continue
    m = s
    while m <= MAX_ID:
        if not sleepy[m]:
            attend[m] = True
        m += s

absent = [0] * (MAX_ID + 1)
for x in range(3, MAX_ID + 1):
    if sleepy[x] or not attend[x]:
        absent[x] = 1
    else:
        absent[x] = 0

prefix = [0] * (MAX_ID + 1)
for i in range(3, MAX_ID + 1):
    prefix[i] = prefix[i-1] + absent[i]

out = []
for S, E in queries:
    out.append(str(prefix[E]- prefix[S-1]))

print('\n'.join(out))