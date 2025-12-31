import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    parts = input().split()
    test_id = int(parts[0])
    arr = list(map(int, parts[1:]))

    line = []
    cnt = 0

    for x in arr:
        i = 0
        while i < len(line) and line[i] < x:
            i += 1
        
        cnt += len(line) - i
        line.insert(i, x)
    
    print(test_id, cnt)

    

