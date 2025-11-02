import sys
input = sys.stdin.readline

N = int(input())
E = int(input())

known = [set() for _ in range(N+1)]
next_song_id = 0

for _ in range(E):
    data = list(map(int, input().split()))
    P = data[0]
    dudes = data[1:]

    if 1 in dudes:
        song = next_song_id
        next_song_id += 1

        for p in dudes:
            known[p].add(song)
    else:
        merged = set()
        for p in dudes:
            merged |= known[p]
        for p in dudes:
            known[p] = set(merged)

all_song = set()
for p in range(1, N+1):
    all_song |= known[p]
for p in range(1, N+1):
    if all_song == known[p]:
        print(p)

    

    

