import heapq

n ,m = map(int, input().split())
gift = list(map(int, input().split()))
children = list(map(int, input().split()))

gift = [-g for g in gift]
heapq.heapify(gift)

children.sort(reverse = True)

for need in children:
    if not gift:
        print(0)
        break
    largest = -heapq.heappop(gift)
    if largest < need:
        print(0)
        break
    remain = largest - need
    if remain > 0:
        heapq.heappush(gift, -remain)
else:
    print(1)







