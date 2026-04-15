import sys
input = sys.stdin.readline

N, K = map(int, input().split())

students = {}

for _ in range(N):
    s, g = map(int, input().split())

    if (s,g) in students:
        students[(s,g)] += 1
    else:
        students[(s,g)] = 1

answer = 0

for cnt in students.values():
    answer += cnt // K
    if cnt % K != 0:
        answer += 1

print(answer)