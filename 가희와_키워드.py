import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = set()
for _ in range(n):
    keyword = input().strip()
    memo.add(keyword)

for _ in range(m):
    keywords = input().strip().split(',')
    
    for k in keywords:
        if k in memo:
            memo.remove(k)
    print(len(memo))