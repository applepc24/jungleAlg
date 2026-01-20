import sys
input = sys.stdin.readline

n = int(input())
used = set()

for _ in range(n):
    s = input().rstrip()
    words = s.split()
    
    picked_index = -1
    
    idx = 0
    for w in words:
        ch = w[0].lower()
        if ch not in used:
            used.add(ch)
            picked_index = idx
            break
        idx += len(w) + 1
    
    if picked_index == -1:
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            low = ch.lower()
            if low not in used:
                used.add(low)
                picked_index = i
                break
    if picked_index == -1:
        print(s)
    else:
        print(s[:picked_index] + '[' + s[picked_index] + ']' + s[picked_index+1:])


