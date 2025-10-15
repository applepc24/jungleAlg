import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    wf = list(map(int, input().split()))
    S = sum(wf)
    
    day = 1
    if S > N:
        print(day)
        continue
    
    while True:
        day += 1
        nxt = [0]*6
        for i in range(6):
            left = wf[(i-1)%6]
            right = wf[(i+1)%6]
            opp = wf[(i+3)%6]
            nxt[i] = wf[i] + left + right + opp
        wf = nxt
        S = sum(wf)
        if S > N:
            print(day)
            break
