import sys
input = sys.stdin.readline

N = int(input())
books = {}

for _ in range(N):
    title = input().strip()
    
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

max_cnt = max(books.values())
answer = ""

for title in sorted(books.keys()):
    if books[title] == max_cnt:
        answer = title
        break

print(answer)