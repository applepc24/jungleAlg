import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w = input().strip()
    k = int(input())

    pos = [[] for _ in range(26)]
    for i, ch in enumerate(w):
        pos[ord(ch) - ord('a')].append(i)
    
    min_len = 10**9
    max_len = 0
    
    for c in range(26):
        p = pos[c]
        if len(p) < k:
            continue
        
        

        for i in range(len(p) - k + 1):
            length = p[i + k - 1] - p[i] + 1

            if length < min_len:
                min_len = length
            if length > max_len:
                max_len = length
            
    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)
       