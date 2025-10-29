import sys
input = sys.stdin.readline

N = int(input())

items = []
for i in range(1, N+1):
    w,h = map(int, input().split())
    score = w*w + h*h
    items.append((score, i))
    items.sort(key=lambda x:(-x[0], x[1]))



for _,i in items:
    print(i)
