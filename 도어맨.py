X = int(input())
line = list(input())

men = women = 0
i = 0

while i < len(line):
    if line[i] == 'M':
        if abs((men + 1) - women) <= X:
            men += 1
            i += 1
        elif i + 1 < len(line) and line[i + 1] == 'W' and abs(men - (women + 1)) <= X:
            women += 1
            line.pop(i + 1)
        else:
            break
    else:
        if abs(men - (women + 1)) <= X:
            women += 1
            i += 1
        elif i + 1 < len(line) and line[i+1] == 'M' and abs((men + 1)- women) <= X:
            men += 1
            line.pop(i+1)
        else:
            break
    
print(men + women)



def solve(n: int, line: str) -> int:
    result = 0
    women = 0
    men = 0
    while True:
        result = women + men
        if len(line) == 0: 
            break
        if abs(women-men) > n:
            result -= 1
            break
        if women > men and len(line) > 1:
            # skip condition
            if line[0] == 'W' and line[1] == 'M' and len(line) > 2:
                line = line[0] + line[2:]
                men += 1
                continue
            else:
                pass
        elif women < men and len(line) > 1:
            if line[0] == 'M' and line[1] == 'W' and len(line) > 2:
                line = line[0] + line[2:]
                women += 1
                continue
            else: 
                pass
        if line[0] == 'M':
            men += 1
        else:
            women += 1
        line = line[1:]
    print(result)