import sys
input = sys.stdin.readline
import math

s= input().strip()

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(s)
if not is_prime(n):
    print('no')
    sys.exit(0)

rotate_map = {
    '0': '0',
    '1': '1',
    '2': '2',
    '5': '5',
    '8': '8',
    '6': '9',
    '9': '6',
}
rot_digits = []
for ch in reversed(s):
    if ch not in rotate_map:
        print('no')
        sys.exit(0)
    rot_digits.append(rotate_map[ch])

rot_str = ''.join(rot_digits)
rot_n = int(rot_str)

if is_prime(rot_n):
    print('yes')
else:
    print('no')
