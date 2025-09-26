N = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

def rps(a, b):
    if a == b:
        return 0
    if a == 1 and b == 3:
        return 1
    if a == 2 and b == 1:
        return 1
    if a == 3 and b == 2:
        return 1
    else:
        return 2

best = 0
streak = 0
prev_winner = None

for i in range(N):
    res = rps(team1[i], team2[i])
    if i == 0:
        winner = 'team1' if res == 1 else 'team2'
    else:
        if res == 0:
            winner = 'team1' if prev_winner == 'team2' else 'team2'
        else:
            winner ='team1' if res == 1 else 'team2'
    if winner == prev_winner:
        streak += 1
    else:
        streak = 1
    
    best = max(best, streak)
    prev_winner = winner

print(best)