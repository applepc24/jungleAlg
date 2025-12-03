import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord('a')] += 1

ans = 0

if max(freq) <= 1:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(fact)
    sys.exit(0)

def dfs(pos, last):
    global ans

    if pos == n:
        ans += 1
        return
    
    for i in range(26):
        if freq[i] == 0:
            continue

        if i == last:
            continue
        
        freq[i] -= 1
        dfs(pos + 1, i)
        freq[i] += 1

dfs(0, -1)
print(ans)
        
