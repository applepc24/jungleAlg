import sys
s = sys.stdin.readline().strip()

pos = [[-1, -1] for _ in range(26)]

for i in range(52):
    c = ord(s[i]) - ord('A')
    if pos[c][0] == -1:
        pos[c][0] = i
    else:
        pos[c][1] = i

ans = 0
for x in range(26):
    ax1 = pos[x][0]
    ax2 = pos[x][1]
    for y in range(x+1 , 26):
        by1 = pos[y][0]
        by2 = pos[y][1]

        cond1 = ax1 < by1 < ax2 < by2
        cond2 = by1 < ax1 < by2 < ax2
        if cond1 or cond2:
            ans += 1
print(ans)