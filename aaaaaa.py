from typing import MutableSequence
'''
arr = [5,8,4,2,6,1,3,9,7]
from typing import MutableSequence

퀵솥트

def qsort(a: MutableSequence, left, right):
    pl = left
    pr = right
    pivot = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while a[pr] > pivot:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)


qsort(arr,0, len(arr)-1)
print(arr)
'''
퀵솥트간단한
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len[0]
    left = []
    right = []

    for element in arr[1::]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    return quick_sort(left)+[pivot]+quick_sort(right)
'''

# 피보나치

# def fibo():
#     a,b = 0,1
#     while True:
#         a,b = b, a+b
#         yield a
# f = fibo()
# next(f)


# def fib_rec(n):
#     if n == 1 or n==2:
#         return 1
#     return fib_rec(n-1) + fib_rec(n-2)
# n = int(input())
# seq = []

# for i in range(1, n+1):
#     seq.append(fib_rec(i))
# print(seq)


# def fib_rec(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n == 0:
#         return 0
#     return fib_rec(n-1) + fib_rec(n-2)

# n = 6
# for i in range(1, n+1):   
#     print(f"fib_rec({i}) = {fib_rec(i)}")

# 에라토스테네스의 체

# def is_prime(x):
#     prime = [True] * (x+1)
#     prime[0] = prime[1] = False

#     for i in range(2, int(math.sqrt(x))+1):
#         if prime[i]:
#             for j in range(i*i, x+1, i):
#                 prime[j] = False
#     return prime


from typing import Any, Sequence

def bin_search(a:Sequence, key: Any ) -> int:
    pl = 0
    pr = len(a) -1
    
    while True:
        pc = (pl + pr) // 2
        if pc < key:
            pl = pc +1
        else:
            pr = pc-1
        if pl > pr:
            break
        return -1

'''
이진트리

from __future__ import annotaions
from typing import Any, Type

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None
'''


'''
병합정렬

from typing import Sequence, MultableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MultableSequence) -> None:

    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa< na and pb<nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1
    
merge_sorted_list(a, b, c)
                