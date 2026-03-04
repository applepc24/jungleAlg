import sys

input = sys.stdin.readline

K = int(input())

S = 1
while S < K:
    S *= 2

need = K
piece = S
cut = 0

while need > 0:
    if need >= piece:
        need -= piece
    else:
        piece //= 2
        cut += 1
print(S, cut)
