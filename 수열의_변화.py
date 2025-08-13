import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

for _ in range(K):
    new_arr = []
    for i in range(len(arr) - 1):
        diff = arr[i+1]-arr[i]
        new_arr.append(diff)
    arr = new_arr

print(','.join(map(str, arr)))