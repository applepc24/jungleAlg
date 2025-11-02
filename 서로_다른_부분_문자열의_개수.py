import sys
input = sys.stdin.readline
S = input().strip()

sub = set()
n = len(S)
for i in range(n):
    for j in range(i+1, n+1):
        sub.add(S[i:j])

print(len(sub))
