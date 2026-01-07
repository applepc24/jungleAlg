import sys
input = sys.stdin.readline
s = input().strip()
i = 0
n = 0

while i < len(s):
    n += 1
    for ch in str(n):
        if ch == s[i]:
            i += 1
            if i == len(s):
                break
print(n)