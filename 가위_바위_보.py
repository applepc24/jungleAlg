def determine_winner(moves):
    unique = set(moves)
    if len(unique) != 2:
        return []

    # 승패 규칙
    beats = {
        'R': 'S',
        'S': 'P',
        'P': 'R'
    }

    a, b = unique
    if beats[a] == b:
        winner, loser = a, b
    elif beats[b] == a:
        winner, loser = b, a
    else:
        return []

    losers = [i for i, move in enumerate(moves) if move == loser]
    return losers

T = int(input())
for _ in range(T):
    N = int(input())
    robots = [input().strip() for _ in range(N)]
    k = len(robots[0])
    alive = list(range(N))
    
    for round_idx in range(k):
        if len(alive) == 1:
            break
        
        current_moves = [robots[i][round_idx] for i in alive]
        losers = determine_winner(current_moves)

        alive = [alive[i] for i in range(len(alive)) if i not in losers]

    if len(alive) == 1:
        print(alive[0] + 1)
    else:
        print(0)

