from typing import Any, Sequence

N = int(input())
check_nums = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split()))

def search(a : Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) -1

    while True:
        pc = (pl+pr)// 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc +1
        else:
            pr = pc -1
        if pl > pr:
            return None

check_nums.sort()

for i in find_nums:
    if search(check_nums, i) is not None:
        print(1)
    else:
        print(0)


