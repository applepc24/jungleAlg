
lines = []

op = int(input())

for _ in range(op):
    lines.append(input())

for line in lines:
    point = 0
    combo = 0
    for ox in line:
        if ox == 'O':
            combo += 1
            point += combo
        else: 
            combo = 0

    print(point)
