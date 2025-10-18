import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    xs = list(map(int, input().split()))
    xs.sort()
    s = set(xs)

    cnt = 0
    for i in range(n):
        xi = xs[i]
        for k in range(i+2, n):
            xk = xs[k]
            ssum = xi + xk
            if ssum & 1:   # 합이 홀수면 중앙값이 정수가 아님
                continue
            mid = ssum // 2
            if mid in s:   # mid가 존재하면 i<j<k 성립
                cnt += 1

    print(cnt)

