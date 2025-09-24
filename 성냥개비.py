N = int(input())

S = [6,2,5,5,4,5,6,3,7,6]

match_2d = [0] * 100
for x in range(100):
    tens = x // 10
    ones = x % 10
    match_2d[x] = S[tens] + S[ones]

plus = 4

def solve():
    for a in range(100):
        for b in range(100):
            s = a + b
            if s >= 100:
                continue
            total = match_2d[a] + match_2d[b] + match_2d[s] + plus
            if total == N:
                print(f"{a:02d}+{b:02d}={s:02d}")
                return
    print("impossible")

solve()
