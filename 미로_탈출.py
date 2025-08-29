import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, S, E = map(int, input().split())
    # 세 구간으로 나눌 수 있음
    # 두 구간인 경우: s, e 중 양끝 점이 하나일 때, s, e가 붙어있을 때
    # 한 구간일 때: N이 2일 때, s, e가 양 끝일 때
    # 어쨌든 각 방을 한 번씩은 방문해야 함
    # 최단 시간에 탈출하는 것이 우선 -> 최대한 겹치지 않게 탈출하기

    if N == 2:
        print(0)
        
    # S랑 E가 붙어있는 경우 
    elif abs(S-E) == 1:
        print(1)

    # s, e 중에 양끝 점이 하나면 1, 두개면 0, 없으면 2
    elif S == 1:
        if E == N:
            print(0)
        else:
            print(1)
    elif S == N:
        if E == 1:
            print(0)
        else:
            print(1)
    else:
        print(2)