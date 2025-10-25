import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    best_cost = 0
    ans = 0
    for i in reversed(num):
        if i > best_cost:
            best_cost = i
        else:
           ans += (best_cost - i)
    print(ans) 

        