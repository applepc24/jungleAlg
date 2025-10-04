import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

if len(S) <= 25:
    print(S)
    sys.exit(0)

L = 11
R = len(S) -12

p = S.find('.', L)


if p != -1 and R <= p:
    print(S[:11] + '...' + S[-11:] )
else:
    print(S[:9] + '......' + S[-10:])