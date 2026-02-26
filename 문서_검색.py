import sys
input = sys.stdin.readline

doc = input().rstrip('\n')
word = input().rstrip('\n')

i = 0
count = 0
L = len(word)

while i <= len(doc) - L:
    if doc[i:i+L] == word:
        count += 1
        i += L
    else:
        i += 1
print(count)