import sys

def to_sec(s):
    m, s = map(int, s.split(':'))
    return m * 60 + s

def to_mmss(x):
    m = x // 60
    s = x % 60
    return f"{m:02d}:{s:02d}"

input = sys.stdin.readline

END = 48*60

N = int(input())
events = []
for _ in range(N):
    team, ts = input().split()
    team = int(team)
    t = to_sec(ts)
    events.append((t, team))

events.sort()

score1 = score2 = 0
lead1 = lead2 = 0
last = 0

for t, team in events:
    if score1 > score2:
        lead1 += t - last
    elif score2 > score1:
        lead2 += t - last
    
    if team == 1:
        score1 += 1
    if team == 2:
        score2 += 2
    
    last = t
    
if score1 > score2:
    lead1 += END - last
elif score1 < score2:
    lead2 += END - last

print(to_mmss(lead1))
print(to_mmss(lead2))


