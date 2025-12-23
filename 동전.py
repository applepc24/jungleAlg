import sys
input = sys.stdin.readline

# 입력 3줄 고정
weighs = []
for _ in range(3):
    parts = input().split()
    # A B C D x E F G H
    left = list(map(int, parts[:4]))
    sign = parts[4]
    right = list(map(int, parts[5:]))
    weighs.append((left, sign, right))

def ok_candidate(fake, delta):
    """
    fake: 가짜 동전 번호 (1..12)
    delta: 무겁다 +1, 가볍다 -1
    """
    for left, sign, right in weighs:
        L = delta if fake in left else 0
        R = delta if fake in right else 0

        if sign == '<':
            if not (L < R):
                return False
        elif sign == '>':
            if not (L > R):
                return False
        else:  # '='
            if not (L == R):
                return False
    return True

cands = []
for coin in range(1, 13):
    if ok_candidate(coin, +1):
        cands.append((coin, '+'))
    if ok_candidate(coin, -1):
        cands.append((coin, '-'))

if len(cands) == 0:
    print("impossible")
elif len(cands) == 1:
    coin, pm = cands[0]
    print(f"{coin}{pm}")
else:
    print("indefinite")