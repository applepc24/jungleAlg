from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx =[0, 0, 0, -1, 1]
dy =[0, -1, 1, 0, 0]

plant = []

for i in range(1, n-1):
    for j in range(1, n-1):
        plant.append((i,j))

def flowerRoad(flowers):
    visited = [[False] * n for _ in range(n)]
    total_cost = 0

    for x, y in flowers:
        for dir in range(5):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if visited[nx][ny]:
                return float('inf')  # 겹침
            visited[nx][ny] = True
            total_cost += board[nx][ny]
    return total_cost
min_cost = float('inf')

allcost = []
for combo in combinations(plant, 3):
    cost = flowerRoad(combo)
    allcost.append(cost)

print(min(allcost))