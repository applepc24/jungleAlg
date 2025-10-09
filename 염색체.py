import sys

def is_AF(ch:str) -> bool:
    return 'A' <= ch <= 'F'

def rule(s : str) -> bool:
    i, n  = 0, len(s)

    def eat_run(ch: str, min_cnt : int) -> bool:
        nonlocal i
        start = i
        while i < n and s[i] == ch:
            i += 1
        return (i-start) >= min_cnt

    def eat_optional_AF() -> None:
        nonlocal i
        if i < n and is_AF(s[i]) and s[i] != 'A':
            i += 1

    eat_optional_AF()

    if not eat_run('A', 1):
        return False

    if not eat_run('F', 1):
        return False

    if not eat_run('C', 1):
        return False
    
    if i < n:
        if i == n -1 and is_AF(s[i]):
            i += 1
        else:
            return False
    
    return i == n

T = int(input())
for _ in range(T):
    s = input().strip()
    print("Infected!" if rule(s) else "Good")