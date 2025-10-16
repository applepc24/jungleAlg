import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

uniq = sorted(set(A))

rank = {}
for i, v in enumerate(uniq):
    rank[v] = i

out = []
for x in A:
    out.append(str(rank[x]))

print(" ".join(out))