import sys
input = sys.stdin.readline

def finalize(score, rewards):
    if 35 <= score < 65:
        rewards[0] += 1
    elif 65 <= score < 95:
        rewards[1] += 1
    elif 95 <= score < 125:
        rewards[2] += 1
    elif score >= 125:
        rewards[3] += 1

def solve():
    N = int(input())
    rolls = list(map(int, input().split()))

    rewards = [0, 0, 0, 0]

    score = 0
    time_passed = 0
    score_per_roll = 1
    time_per_turn = 4

    i = 0
    while i < N:
        if time_passed > 240:
            finalize(score, rewards)
            score = 0
            time_passed = 0
            score_per_roll = 1
            time_per_turn = 4
            continue
        
        d = rolls[i]

        if d == 1:
            finalize(score, rewards)
            score = 0
            time_passed = 0
            score_per_roll = 1
            time_per_turn = 4
            i += 1
            continue
        if d == 2:
            if score_per_roll > 1:
                score_per_roll //= 2
            else: time_per_turn += 2
        elif d == 5:
            if time_per_turn > 1:
                time_per_turn -= 1
        elif d == 6:
            if score_per_roll < 32:
                score_per_roll *= 2
        
        score += score_per_roll

        add_time = time_per_turn

        if d == 4:
            add_time += 56
        time_passed += add_time

        i += 1
    print(rewards[0])
    print(rewards[1])
    print(rewards[2])
    print(rewards[3])

solve()