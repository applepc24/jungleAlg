import sys
input = sys.stdin.readline

S = input().strip()

NS = S[0]

for ch in S[1:]:
    if ch <= NS[0]:
        NS = ch + NS
    else:
        NS = NS + ch

print(NS)