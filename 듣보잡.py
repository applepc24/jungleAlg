import sys
input = sys.stdin.readline

N, M = map(int, input().split())

D = set(input().strip() for _ in range(N))

answer = []
for _ in range(M):
    B = input().strip()
    if B in D:
        answer.append(B)

print(len(answer))
print('\n'.join(answer))