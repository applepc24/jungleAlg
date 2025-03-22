from typing import Any

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(str, input())))

def check_string(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        
        if cnt < 0:
            return 'NO'
    
    if cnt == 0:
        return 'YES'
    else:
        return 'NO'

for string in arr:
    print(check_string(string))
        
