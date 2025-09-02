import math

a, b, h = map(int, input().split())

if a == b:
    print(-1)
else:
    delta = abs(b - a)
    s_squared = delta ** 2 + h ** 2
    result = math.pi * s_squared * (a + b) / delta
    print(f"{result:.9f}")