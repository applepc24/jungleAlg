import sys
input = sys.stdin.readline

t= int(input())
serials = [input().strip() for _ in range(t)]

def sum_of_digit(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            ch = int(ch)
            total += ch
    return total

serials.sort(key = lambda s:(len(s), sum_of_digit(s), s))

print("\n".join(serials))
