import sys
input = sys.stdin.readline

N, S, R = map(int, input().split())
broken = set(map(int, input().split()))
reserve = set(map(int, input().split()))

both = broken & reserve
broken -= both
reserve -= both

for r in sorted(reserve):
    if r - 1 in broken:
        broken.remove(r-1)
    elif r + 1 in broken:
        broken.remove(r+1)

print(len(broken))