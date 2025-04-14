import sys
input = sys.stdin.readline

def solve(left, right):
    # 구간이 하나일 경우 ➔ 높이 그대로 반환
    if left == right:
        return heights[left]

    # 중앙 인덱스
    mid = (left + right) // 2

    # 왼쪽 구간 최대 넓이 (재귀)
    left_area = solve(left, mid)

    # 오른쪽 구간 최대 넓이 (재귀)
    right_area = solve(mid + 1, right)

    # 중앙을 걸치는 최대 넓이
    cross_area = max_cross_area(left, mid, right)

    # 이 셋 중에서 최대값 반환!
    return max(left_area, right_area, cross_area)


def max_cross_area(left, mid, right):
    # 가운데 두 칸에서 시작 ➔ mid와 mid+1
    lo = mid
    hi = mid + 1

    # 처음 최소 높이
    height = min(heights[lo], heights[hi])

    # 초기 넓이 ➔ 두 칸
    max_area = height * 2

    # 좌우로 확장하면서 최대 넓이를 찾기
    while left < lo or hi < right:
        # 오른쪽으로 확장할 수 있고,  
        # 왼쪽이 경계에 다다랐거나 오른쪽이 더 높을 경우
        if hi < right and (lo == left or heights[lo - 1] < heights[hi + 1]):
            hi += 1
            height = min(height, heights[hi])
        else:
            lo -= 1
            height = min(height, heights[lo])

        width = hi - lo + 1
        max_area = max(max_area, height * width)

    return max_area


while True:
    # 입력 받기 (첫 번째 숫자가 0이면 종료)
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    n = line[0]
    heights = line[1:]

    # 전체 구간에 대한 최대 넓이 구하기
    print(solve(0, n - 1))