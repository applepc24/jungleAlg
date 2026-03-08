import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()

i = 0
cnt = 0

while i < len(P):
    max_len = 0

    for j in range(len(S)):
        k = 0
        while j + k < len(S) and i + k < len(P) and P[i+k] == S[j+k]:
            k += 1
        max_len = max(max_len, k)
    i += max_len
    cnt += 1

print(cnt)