N = int(input())

odd_idx = []
even_idx = []

for i in range(1, N+1):
    x, y  = map(int, input().split())
    if (x + y) & 1:
        odd_idx.append(i)
    else:
        even_idx.append(i)

if not odd_idx or not even_idx:
    print('NO')
else:
    print('YES')
    order = odd_idx + even_idx
    print(" ".join(map(str, order)))
