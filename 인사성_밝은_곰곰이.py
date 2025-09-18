
N = int(input())
ans = 0
seen = set()

for _ in range(N):
    s= input()
    if s == "ENTER":
        seen.clear()
    else:
        if s not in seen:
            ans += 1
            seen.add(s)
    
print(ans)