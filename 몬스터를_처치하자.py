import sys
input = sys.stdin.readline

N, Hp = map(int, input().split())
C = []
D = []
for _ in range(N):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

states = { tuple([0]*N) : 0}

t = 0
while True:
    nxt = {}

    for cd, dmg in states.items():
        cd_list = []
        for i in range(N):
            x = cd[i]
            if x > 0:
                cd_list.append(x-1)
            else:
                cd_list.append(0)
        wait_cd_tuple = tuple(cd_list)

        if wait_cd_tuple in nxt:
            if dmg > nxt[wait_cd_tuple]:
                nxt[wait_cd_tuple] = dmg
        else:
            nxt[wait_cd_tuple] = dmg
        
        for i in range(N):
            if cd[i] == 0:
                new_cd_list = []
                for j in range(N):
                    val = cd[j]
                    if val > 0:
                        new_cd_list.append(val -1)
                    else:
                        new_cd_list.append(0)
                
                new_cd_list[i] = C[i] -1
                new_cd_tuple = tuple(new_cd_list)

                new_dmg = dmg + D[i]

                if new_dmg >= Hp:
                    print(t + 1)
                    sys.exit(0)
                
                if new_cd_tuple in nxt:
                    if new_dmg > nxt[new_cd_tuple]:
                        nxt[new_cd_tuple] = new_dmg
                else:
                    nxt[new_cd_tuple] = new_dmg
    states = nxt
    t += 1