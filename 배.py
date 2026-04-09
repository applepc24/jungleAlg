import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()

position = [0] * N
checked = [False] * M
count = 0
time = 0

while count < M:
    for i in range(N):
        while position[i] < M:
            if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                checked[position[i]] = True
                count += 1
                position[i] += 1
                break
            position[i] += 1
    time += 1

print(time)