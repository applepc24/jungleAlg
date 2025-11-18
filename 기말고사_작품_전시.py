import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    w = [[0] * N for _ in range(N)]
    
    for _ in range(M):
        V, A, B = map(int, input().split())
        A -= 1
        B -= 1
        w[A][B] += V
    
    max_score = -10 ** 18
    ways = 0

    for perm in permutations(range(N)):
        score = 0
        for i in range(N):
            u = perm[i]
            for j in range(i+1, N):
                v = perm[j]
                score += w[u][v]
        if score > max_score:
            max_score = score
            ways = 1
        elif score == max_score:
            ways += 1
    
    print(max_score, ways)
