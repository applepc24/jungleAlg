import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
cap = [0] + list(map(int, input().split()))

remain = cap[:]


first_apply = [set() for _ in range(M+1)]
total_apply = [set() for _ in range(M+1)]

enrolled = [set() for _ in range(N+1)]

for stu in range(1, N + 1):
    for x in map(int, input().split()):
        if x == -1:
            break
        first_apply[x].add(stu)
        total_apply[x].add(stu)

for stu in range(1, N + 1):
    for x in map(int, input().split()):
        if x == -1:
            break
        total_apply[x].add(stu)
for c in range(1, M + 1):
    cnt = len(first_apply[c])
    if cnt <= remain[c]:
        for stu in first_apply[c]:
            enrolled[stu].add(c)
        remain[c] -= cnt

for c in range(1, M+1):
    if remain[c] <= 0:
        continue
    applicants = total_apply[c] - {stu for stu in range(1, N+1) if c in enrolled[stu]}
    cnt = len(applicants)
    if cnt <= remain[c]:
        for stu in applicants:
            enrolled[stu].add(c)
        remain[c] -= cnt

for stu in range(1, N+1):
    if not enrolled[stu]:
        print("망했어요")
    else:
        print(*sorted(enrolled[stu]))