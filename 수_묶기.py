import sys
input = sys.stdin.readline

N = int(input())

plus = []
minus = []
one = 0
zero = 0

for _ in range(N):
    x = int(input())

    if x > 1:
        plus.append(x)
    elif x == 1:
        one += 1
    elif x == 0:
        zero += 1
    elif x < 0:
        minus.append(x)

plus.sort(reverse=True)
minus.sort()

answer = 0

for i in range(0, len(plus) - 1, 2):
    answer += plus[i] * plus[i+1]

if len(plus) % 2 == 1:
    answer += plus[-1]

answer += one

for i in range(0, len(minus)-1, 2):
    answer += minus[i] * minus[i+1]

if len(minus) % 2 == 1:
    if zero == 0:
        answer += minus[-1]

print(answer)
