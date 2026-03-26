import sys
input = sys.stdin.readline

N = int(input())

ans = 0

for _ in range(N):
    s = input().strip()
    seen = set()
    prev = ''
    
    is_group = True

    for ch in s:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch
    
    if is_group:
        ans += 1

print(ans)
