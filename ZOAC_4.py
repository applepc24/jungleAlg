import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

row_count = (h + (n+1) - 1) // (n+1)
col_count = (w + (m+1) - 1) // (m+1)
print(row_count * col_count)