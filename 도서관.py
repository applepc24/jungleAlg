import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book_loca = list(map(int, input().split()))

plus = []
minus = []

for x in book_loca:
    if x > 0:
        plus.append(x)
    else:
        minus.append(-x)
    
plus.sort(reverse=True)
minus.sort(reverse=True)

def get_dist(arr):
    dist = []
    for i in range(0, len(arr), m):
        dist.append(arr[i])
    return dist

plus_dist = get_dist(plus)
minus_dist = get_dist(minus)

answer = 0
for x in plus_dist:
    answer += x * 2
for x in minus_dist:
    answer += x * 2

max_dist = 0
if plus_dist:
    max_dist = max(max_dist, plus_dist[0])
if minus_dist:
    max_dist = max(max_dist, minus_dist[0])

answer -= max_dist
print(answer)