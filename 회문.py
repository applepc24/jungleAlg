import sys
input = sys.stdin.readline

def felin(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    return True

def solve(s: str) -> int:
    l, r = 0, len(s) -1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if felin(s, l+1, r) or felin(s, l, r-1):
                return 1
            return 2
    return 0

T = int(input())
for _ in range(T):
    S = input().strip()
    print(solve(S))
