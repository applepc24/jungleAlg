import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
ans = 0

for _ in range(N):
    nums = list(map(int, input().split()))
    cnt = Counter(nums)

    if len(cnt) == 1:
        x = nums[0]
        money = 50000 + x * 5000
    elif len(cnt) == 2:
        items = list(cnt.items())
        
        if items[0][1] == 3 or items[1][1] == 3:
            for num, c in items:
                if c == 3:
                    money = 10000 + num * 1000
                    break
        else:
            a = items[0][0]
            b = items[1][0]
            money = 2000 + a * 500 + b * 500
    elif len(cnt) == 3:
        for num, c in cnt.items():
            if c == 2:
                money = 1000 + num * 100
                break
    
    else:
        money = max(nums) * 100
    
    ans = max(ans, money)
print(ans)