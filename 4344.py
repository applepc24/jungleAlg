numbers = []

t = int(input())
for _ in range(t):
    numbers.append(list(map(int, input().split())))

for number in numbers:
    n = number[0]
    scores = number[1:] 
    total = sum(scores)
    avr = total / n

    up = []
    for i in scores:
        if i > avr:
            up.append(i)

    
    case = len(up) / n * 100

    
    print(f"{case:.3f}%")
