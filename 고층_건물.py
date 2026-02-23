import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

def view(a_num, a_den, b_num, b_den):
    return a_num * b_den > b_num * a_den

ans = 0

for i in range(n):
    cnt = 0

    has_best = False
    best_num = best_den = 1
    for j in range(i+1, n):
        num = h[j] - h[i]
        den = j - i
        if not has_best or view(num, den, best_num, best_den):
            cnt += 1
            best_num, best_den = num, den
            has_best = True
    
    has_best = False
    best_num = best_den = 1
    for j in range(i-1, -1, -1):
        num = h[j] - h[i]
        den = i - j
        if not has_best or view(num, den, best_num, best_den):
            cnt += 1
            best_num, best_den = num, den
            has_best = True
    
    ans = max(ans, cnt)

print(ans)