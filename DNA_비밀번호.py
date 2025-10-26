import sys
input = sys.stdin.readline

S_len, P = map(int, input().split())
S = input().strip()
a, c, g, t = map(int, input().split())
need = [a, c, g, t]

def idx(ch):
    if ch == 'A':
        return 0
    if ch == 'C':
        return 1
    if ch == 'G':
        return 2
    return 3

count = [0, 0, 0, 0]

for i in range(P):
    count[idx(S[i])] += 1

def ok():
    for i in range(4):
        if count[i] < need[i]:
            return False
    return True

answer = 0
if ok():
    answer += 1

for start in range(1, S_len - P + 1):
    left_char = S[start -1]
    count[idx(left_char)] -= 1

    right_char = S[start + P - 1]
    count[idx(right_char)] += 1

    if ok():
        answer += 1

print(answer)    

