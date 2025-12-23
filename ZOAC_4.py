import sys
input = sys.stdin.readline

H, W, i, j = map(int, input().split())

rows = (H + (i+1) -1) // (i+1)
cols = (W + (j+1) -1) // (j+1)
print(rows * cols)