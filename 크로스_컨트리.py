import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = {}
    for team in arr:
        if team in cnt:
            cnt[team] += 1
        else:
            cnt[team] = 1
    
    vaild = set()
    for team, c in cnt.items():
        if c == 6:
            vaild.add(team)
    
    scores = {}
    score = 1
    for team in arr:
        if team in vaild:
            if team not in scores:
                scores[team] = []
            scores[team].append(score)
            score += 1
    
    best_team = -1
    best_sum4 = 10**18
    best_fifth = 10**18

    for team in vaild:
        sum4 = scores[team][0] + scores[team][1] + scores[team][2] + scores[team][3]
        fifth = scores[team][4]

        if sum4 < best_sum4:
            best_team = team
            best_sum4 = sum4
            best_fifth = fifth
        elif sum4 == best_sum4:
            if fifth < best_fifth:
                best_team = team
                best_fifth = fifth
    print(best_team)