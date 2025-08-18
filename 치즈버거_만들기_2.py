import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A <= B or (A - B) > B:
    print('NO')
    sys.exit(0)

buger = A - B
print('YES')
print(K)

for _ in range(K -1):
    print('aba')

last_buger = B - (K - 1)
print("ab" * last_buger + 'a')