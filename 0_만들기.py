import sys

input = sys.stdin.readline

T = int(input())


def solve(n: int):
    out = []

    def dfs(idx, expr, total, sign, cur):
        if idx == n + 1:
            if total + sign * cur == 0:
                out.append(expr)
            return

        dfs(idx + 1, expr + " " + str(idx), total, sign, cur * 10 + idx)

        dfs(idx + 1, expr + "+" + str(idx), total + sign * cur, +1, idx)

        dfs(idx + 1, expr + "-" + str(idx), total + sign * cur, -1, idx)

    dfs(2, "1", 0, +1, 1)
    return out


for tc in range(T):
    n = int(input())
    ans = solve(n)
    print("\n".join(ans))
    if tc != T-1:
        print()
