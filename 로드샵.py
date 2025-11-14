import sys
import math

n,m,r = map(int, input().split())

def combi(n: int, r: int) -> int:
    return math.comb(r + (n-1), n-1)

def combi_count(n:int, m: int, r: int) -> int:
    count_m = r-(n*m)
    if count_m < 0:
        return 0
    return combi(n, count_m)

print(combi_count(n,m,r))