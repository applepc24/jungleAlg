import sys
input = sys.stdin.readline

a2, a1, a0 = map(int, input().split())
c= int(input())
n0 = int(input())

ok = True
for n in range(n0, 100):
    fn = a2 * n * n + a1 * n + a0
    if fn > c * n * n:
        ok = False
        break

if ok:
    print(1)
else:
    print(0)