import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    best_num = 0
    ans = 0
    
    arr = arr[::-1]
    for num in arr:
        if best_num <= num:
            best_num = num
        else:
            ans += (best_num - num)
    print(ans)