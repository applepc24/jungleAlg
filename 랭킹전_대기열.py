import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    placed = False

    for room in rooms:
        if len(room["player"]) < m:
            base = room["base"]

            if base -10 <= l <= base +10:
                room["player"].append((l,n))
                placed = True
                break
            
    if not placed:
        rooms.append({
            "base" : l,
            "player" : [(l, n)]
        })

for room in rooms:
    if len(room["player"]) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    room["player"].sort(key = lambda x: x[1])

    for lv, nm in room["player"]:
        print(lv, nm)


