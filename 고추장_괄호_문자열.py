import sys
input = sys.stdin.readline

N = int(input().strip())
S = list(input().strip())

OPEN_TOTAL = N // 2
ans = S[:]  # 결과 버퍼

def dfs(idx, open_used, balance):
    close_used = idx - open_used

    if open_used > OPEN_TOTAL:
        return False
    if close_used > OPEN_TOTAL:
        return False
    
    if balance < 0:
        return False
    
    if idx == N:
        if balance == 0 and open_used == OPEN_TOTAL:
            print(''.join(ans))
            return True
        return False
    
    ch = S[idx]
    if ch == '(':
        ans[idx] = '('
        return dfs(idx + 1, open_used + 1, balance + 1)
    
    elif ch == ')':
        ans[idx] = '('
        return dfs(idx +1, open_used, balance -1)
    
    else:
        if open_used < OPEN_TOTAL:
            ans[idx] = '('
            if dfs(idx + 1, open_used + 1, balance + 1):
                return True
            
        if balance > 0 and (idx - open_used) < OPEN_TOTAL:
            ans[idx] = ')'
            if dfs(idx + 1, open_used, balance - 1):
                return True

        ans[idx] = 'G'
        return False

dfs(0, 0, 0)    