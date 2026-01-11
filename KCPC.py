import sys
input =sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())

    best = [[0] * (k+1) for _ in range(n+1)]
    subcnt = [0] * (n+1)
    last = [0] * (n+1)

    for idx in range(1, m+1):
        i, j, s = map(int, input().split())
        
        subcnt[i] += 1
        last[i] = idx
        best[i][j] = max(best[i][j], s)
    total = [0] * (n+1)
    for team in range(1, n+1):
        s = 0
        for prob in range(1, k+1):
            s += best[team][prob]
        total[team] = s
    
    ranking = list(range(1, n+1))
    ranking.sort(key = lambda team: (-total[team], subcnt[team], last[team]))
    print(ranking.index(t) + 1)
