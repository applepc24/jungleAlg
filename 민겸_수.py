import sys
s = sys.stdin.readline().strip()

max_parts = []
cnt = 0

for ch in s:
    if ch == 'M':
        cnt += 1
    else:
        if cnt > 0:
            max_parts.append('5' + '0'*cnt)
            cnt = 0
        else:
            max_parts.append('5')
if cnt > 0:
    max_parts.append('1' * cnt)

max_value = ''.join(max_parts)

min_parts = []
cnt = 0

for ch in s:
    if ch == 'M':
        cnt += 1
    else:
        if cnt > 0:
            min_parts.append('1' + '0'*(cnt-1) + '5')
            cnt = 0
        else:
            min_parts.append('5')
        
if cnt > 0:
    min_parts.append('1' + '0'*(cnt-1))

min_value = "".join(min_parts)

print(max_value)
print(min_value)