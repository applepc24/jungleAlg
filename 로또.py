import sys
input = sys.stdin.readline

def solve_case(S):
    path = []
    def dfs(start):
        if len(path) == 6:
            print(*path)
            return
        for i in range(start, len(S)):
            path.append(S[i])
            dfs(i + 1)
            path.pop()
    dfs(0)


def main():
    first = True
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if parts[0] == 0:
            break
        
        if not first:
            print()
        first = False
        
        S= parts[1:]
        solve_case(S)

main()
    