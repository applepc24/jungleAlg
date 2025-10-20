import sys
input = sys.stdin.readline
n, m ,q = map(int, input().split())

accepted = [[False] * (m+1) for _ in range(n + 1)]
wrong = [[0] * (m+1) for _ in range(n+1)]
solved = [0] * (n + 1)
total = [0] * (n + 1)

for _ in range(q):
    t, team, prob, res = input().split()
    t = int(t); team = int(team); prob = int(prob)

    if accepted[team][prob]:
        continue

    if res == "AC":
        accepted[team][prob] = True
        solved[team] += 1
        total[team] += t+ 20* wrong[team][prob]
    else:
        wrong[team][prob] += 1
    
ranking = []
for team_id in range(1, n + 1):
    ranking.append((team_id, solved[team_id], total[team_id]))
ranking.sort(key=lambda x:(x[0], -x[1], -x[2]))

out = []
for tid, s ,tt in ranking:
    out.append(f"{tid} {s} {tt}")
print('\n'.join(out))