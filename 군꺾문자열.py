import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# b가 2의 거듭제곱인지 체크 (비트 안 씀)
def is_power_of_two(x: int) -> bool:
    if x <= 0:
        return False
    while x % 2 == 0:
        x //= 2
    return x == 1

if not is_power_of_two(b):
    print(-1)
    sys.exit(0)

ops = []  # 역방향으로 쌓고, 마지막에 뒤집어서 출력

# 역그리디: (a, b) -> (0, 1)로 줄이기
while True:
    if b == 1:
        # 이제 남은 건 G만 가능: a번 G
        ops.append('G' * a)
        break

    if a >= b:
        a -= b
        ops.append('G')   # 정방향에선 맨 뒤 'G'가 하나 추가된 것
    else:
        b //= 2
        ops.append('K')   # 정방향에선 맨 뒤 'K'가 하나 추가된 것

# 역순으로 모은 걸 뒤집어 정방향으로
print(''.join(reversed(ops)))