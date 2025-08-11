n = int(input())
k = int(input())

if k >= n:
    print(0)
    exit()

positions = list(map(int, input().split()))
positions.sort()

diff = []
for i in range(n-1):
    diff.append(positions[i+1]-positions[i])

diff.sort()

print(sum(diff))