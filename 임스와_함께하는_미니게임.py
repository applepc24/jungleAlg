import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
seen = set()
for _ in range(N):
    name = input().strip()
    seen.add(name)

U = len(seen)
if game == 'Y':
    game = 1
elif game == 'F':
    game = 2
elif game == 'O':
    game = 3

print(U // game)