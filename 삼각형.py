import math

def distance(p1, p2):
    return math.dist(p1,p2)

def is_colinear(a, b, c):
    cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return math.isclose(cross, 0, abs_tol=1e-9)

def triangle_type_by_angle(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides
    x2, y2, z2 = x*x, y*y, z*z
    if math.isclose(x2 + y2, z2, rel_tol=1e-9):
        return "Jikkak"
    elif x2 + y2 > z2:
        return "Yeahkak"
    else:
        return "Dunkak"

def classify_triangle(p1, p2, p3):
    if is_colinear(p1, p2, p3):
        return "X"
    
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)

    if math.isclose(a,b) and math.isclose(b,c):
        return "JungTriangle"
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(c, a):
        angle_type = triangle_type_by_angle(a, b, c)
        return angle_type + "2Triangle"
    else:  # 일반 삼각형
        angle_type = triangle_type_by_angle(a, b, c)
        return angle_type + "Triangle"

points = [tuple(map(int, input().split())) for _ in range(3)]
print(classify_triangle(*points))