import sys

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    p1, p2 = map(int, input().split())
    M = int(input().strip())
    S = int(input().strip())

    INF = 10**18

    # carrier=P, blocker=Q, is_left=True  -> carrier가 p1
    #                       is_left=False -> carrier가 p2
    def cost(P, Q, is_left):
        d_PM = abs(P - M)
        # M 도달 이동횟수는 홀수여야 고기 부착 가능
        if d_PM % 2 == 0:
            return INF

        # 구간 제약 [L, U]을 만들고, blocker 최종 위치를 그 안에서 최소 이동으로 맞추는 전략
        L = -INF
        U = INF

        # 1) P→M 구간에 Q가 끼어 있으면, Q를 M 바깥으로 밀어야 함
        if min(P, M) < Q < max(P, M):
            if P < M:
                # Q가 M을 넘어 오른쪽으로 가야 함: 첫 M 도달이 짝수 이동이어야 고기 안 집음
                if (M - Q) % 2 == 1:
                    return INF
                L = max(L, M + 1)
            else:
                # P > M: Q가 왼쪽으로 가야 함
                if (Q - M) % 2 == 1:
                    return INF
                U = min(U, M - 1)

        # 2) M→S 구간 처리
        #    (a) S > M: 구간 [M..S] 안(끝점 포함)에 Q가 있거나,
        #               1)에서 이미 Q를 M의 오른쪽으로 보내기로 했다면 → S+1 이상으로
        if S > M:
            if (M <= Q <= S) or (L >= M + 1):
                L = max(L, S + 1)
        #    (b) S < M: 구간 [S..M] 안(끝점 포함)에 Q가 있거나,
        #               1)에서 이미 Q를 M의 왼쪽으로 보내기로 했다면 → S-1 이하로
        if S < M:
            if (S <= Q <= M) or (U <= M - 1):
                U = min(U, S - 1)

        # 3) 순서 보존 제약(p1 < p2)
        if is_left:
            # carrier=P=p1 -> blocker는 항상 p1보다 오른쪽에 있어야 함
            L = max(L, P + 1)
        else:
            # carrier=P=p2 -> blocker는 항상 p2보다 왼쪽에 있어야 함
            U = min(U, P - 1)

        # 4) 팬 경계와의 교집합
        L = max(L, 1)
        U = min(U, N)
        if L > U:
            return INF  # 불가능

        # 5) blocker 최소 이동: Q를 [L,U]에 끼워넣기
        if Q < L:
            move_blocker = L - Q
        elif Q > U:
            move_blocker = Q - U
        else:
            move_blocker = 0

        # 총 이동: blocker 이동 + P→M + M→S
        return move_blocker + d_PM + abs(S - M)

    ans = min(cost(p1, p2, True), cost(p2, p1, False))
    print(ans if ans < INF else -1)

solve()

