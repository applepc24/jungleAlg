import sys
input = sys.stdin.readline

n,k,p,x = map(int, input().split())

LED_STR = [
    "1111110",
    "0110000",
    "1101101",
    "1111001",
    "0110011",
    "1011011",
    "1011111",
    "1110000",
    "1111111",
    "1111011",
]

def diff_digit(a:int, b:int) -> int:
    sa, sb = LED_STR[a], LED_STR[b]
    cnt = 0
    for i in range(7):
        if sa[i] != sb[i]:
            cnt += 1
    return cnt


cost = [[0] * 10 for _ in range(10)]
for a in range(10):
    for b in range(10):
        cost[a][b] = diff_digit(a, b)

x_str = str(x).zfill(k)

ans = 0
for y in range(1, n+1):
    if y == x:
        continue
    y_str = str(y).zfill(k)

    flips = 0
    for i in range(k):
        flips += cost[int(x_str[i])][int(y_str[i])]
        if flips > p:
            break
    
    if 1 <= flips <= p:
        ans += 1

print(ans)