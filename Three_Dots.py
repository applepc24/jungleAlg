import sys
input =sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    cnt = 0
    for j in range(1 , n - 1):
        target = 2 * a[j]
        i , k = j -1, j + 1

        while i >= 0 and k < n:
            asum = a[i] + a[k]
            if asum == target:
                cnt += 1
                i -= 1
                k += 1
            elif asum < target:
                k += 1
            elif asum > target:
                i -= 1
    print(cnt)

