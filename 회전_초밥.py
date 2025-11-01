import sys
input= sys.stdin.readline

N, D, K, C = map(int, input().split())

belt = [int(input().strip()) for _ in range(N)]

extended = belt + belt[:K]

count = [0] * (D+1)
unique_cnt = 0

for i in range(K):
    x = extended[i]
    if count[x] == 0:
        unique_cnt += 1
    count[x] += 1

best = 0

for s in range(N):
    curr = unique_cnt

    if count[C] == 0:
        curr += 1
    
    if curr > best:
        best = curr
    
    left_sushi = extended[s]
    count[left_sushi] -= 1
    if count[left_sushi] == 0:
        unique_cnt -= 1
    
    right_sushi = extended[s+ K]
    if count[right_sushi] == 0:
        unique_cnt += 1
    count[right_sushi] += 1

print(best)