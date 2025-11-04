N = int(input())
digits = [0, 1, 2]
cnt = 0

def dfs(pos, total):
    global cnt
    if pos == N:
        if total % 3 == 0:
            cnt += 1
        return

    for d in digits:
        if d == 0 and pos == 0:
            continue
        dfs(pos + 1, total + d)

dfs(0, 0)
print(cnt)