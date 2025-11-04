import sys
input = sys.stdin.readline

s = input().strip()
def solve(s, cnt):
    if len(s)== 1:
        return cnt, int(s)
    
    total = 0
    for i in s:
        total = total + int(i)

    return solve(str(total), cnt + 1)


cnt, num = solve(s, 0)

print(cnt)
if num % 3 == 0:
    print("YES")
else:
    print("NO")

