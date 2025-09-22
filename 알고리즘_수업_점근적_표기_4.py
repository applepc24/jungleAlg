import sys
input = sys.stdin.readline

a2, a1, a0 = map(int, input().split())
c= int(input())
n0 = int(input())

x = c - a2
y = -a1
z = -a0

def phi_at(n):
    return x * n * n + y * n + z

if x < 0:
    print(0)
elif x == 0:
    if y < 0:
        print(0)
    else:
        print(1 if phi_at(n0) >= 0 else 0)
else:
    is_vertex_right = (2 * x * n0) < (-y)
    is_min_negative = (y * y) > (4 * x * z)
    if is_vertex_right and is_min_negative:
        print(0)
    else:
        print(1 if phi_at(n0) >= 0 else 0)
