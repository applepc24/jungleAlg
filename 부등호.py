k = int(input())
signs = input().split()

def ok(a, b, op):
    return (a < b) if op == "<" else(a>b)

visited = [False] * 10
pick = []
min_ans = None
max_ans = None

def dfs(start):
    global min_ans, max_ans
    if start == k + 1:
        ans = ''.join(map(str, pick))
        if min_ans is None or ans < min_ans:
            min_ans = ans
        if max_ans is None or ans > max_ans:
            max_ans = ans
        return
    
    for i in range(10):
        if visited[i]:
            continue
        if start > 0 and not ok(pick[-1], i, signs[start - 1]):
            continue
        visited[i] = True
        pick.append(i)
        dfs(start + 1)
        pick.pop()
        visited[i] = False

dfs(0)
print(max_ans)
print(min_ans)