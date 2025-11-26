import sys
input = sys.stdin.readline

s = input().strip()

def is_pal(s: str) -> bool:
    return s == s[::-1]

for i in range(len(s)):
    if is_pal(s[i:]):
        answer = len(s) + i
        break

print(answer)