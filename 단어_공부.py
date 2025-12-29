import sys
input = sys.stdin.readline
c = input().strip().upper()

cnt = [0] * 26
for ch in c:
    cnt[ord(ch) - ord('A')] += 1
mx = max(cnt)
if cnt.count(mx) > 1:
    print('?')
else:
    print(chr(cnt.index(mx) + ord('A')))

