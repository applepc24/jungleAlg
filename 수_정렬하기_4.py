import sys
input = sys.stdin.readline

N = int(input())
answer = []
for _ in range(N):
    num = int(input())
    answer.append(num)

answer.sort(reverse = True)
print('\n'.join(map(str, answer)))