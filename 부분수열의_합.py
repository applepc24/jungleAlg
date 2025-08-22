def solve():
    import sys
    input = sys.stdin.readline

    N,S = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0

    def dfs(idx, total):
        nonlocal count
        if idx == N:
            if total == S:
                count += 1
            return
        

        dfs(idx + 1, total +arr[idx])
        dfs(idx +1, total)
    
    dfs(0,0)

    if S == 0:
        count -= 1
    
    print(count)

solve()


