N = int(input())
ans = 0 
m = N
while m >= 2:
    ans += (m -1)
    m -= 1
print(ans)