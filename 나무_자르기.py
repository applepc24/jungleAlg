import sys

tree_num, take_tree_num = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

cut_low = 0
cut_high = max(trees)
result = 0

while cut_low <= cut_high:
    mid = (cut_low + cut_high) // 2
    total =0

    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= take_tree_num:
        result = mid
        cut_low = mid + 1
    else:
        cut_high = mid - 1

print(result)






