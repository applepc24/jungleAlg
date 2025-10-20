import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    name, score, risk, cost = input().split()
    score, risk, cost = map(int, (score, risk, cost))
    ans = (score ** 3) // (cost * (risk + 1))
    students.append((name, ans, cost))

students.sort(key = lambda x:(-x[1], x[2], x[0]))

print(students[1][0])