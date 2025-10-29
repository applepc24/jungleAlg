import sys
input = sys.stdin.readline

N = int(input().strip())
covered = [[False] * 501 for _ in range(501)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        row = covered[x]
        for y in range(y1, y2):
            row[y] = True

ans = 0 
for x in range(501):
    ans += sum(covered[x])

print(ans)