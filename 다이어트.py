import sys
input  = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())

foods = [list(map(int, input().split())) for _ in range(N)]

best_cost = float('inf')
best_path = []

def dfs(idx, p, f, s, v,cost, path):
    global best_cost, best_path

    if p>=mp and f>=mf and s>=ms and v>mv:
        if best_cost > cost:
            best_cost = cost
            best_path = path[:]
        elif cost == best_cost and path < best_path:
            best_path = path[:]
    
    if idx == N:
        return 0
    
    dfs(idx+1, p + foods[idx][0], f + foods[idx][1], s + foods[idx][2], v + foods[idx][3],cost + foods[idx][4], path + [idx+1])
    dfs(idx+1, p,f,s,v,cost,path)

dfs(0,0,0,0,0,0,[])

if best_cost == float('inf'):
    print(-1)
else:
    print(best_cost)
    print(*best_path)


