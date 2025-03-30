from collections import deque

def play_snake_game(n, apples, direction_changes):
    # 방향: 오른쪽, 아래, 왼쪽, 위 (시계 방향)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0  # 처음은 오른쪽

    # 보드 초기화 (사과 표시)
    board = [[0] * n for _ in range(n)]
    for x, y in apples:
        board[x][y] = 1  # 사과 위치는 1로 표시

    # 뱀 초기화
    snake = deque()
    snake.append((0, 0))  # 시작 위치
    visited = set()
    visited.add((0, 0))  # 몸통 위치 기억

    time = 0
    direction_idx = 0
    turn_times = sorted(direction_changes.keys())

    while True:
        time += 1
        head_x, head_y = snake[-1]
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]

        # 벽 or 자기 몸에 부딪힘
        if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in visited:
            return time

        # 이동
        snake.append((nx, ny))
        visited.add((nx, ny))

        # 사과가 있다면 → 안 줄임
        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            tail = snake.popleft()
            visited.remove(tail)

        # 방향 전환 시간 확인
        if time in direction_changes:
            if direction_changes[time] == 'D':
                direction = (direction + 1) % 4  # 오른쪽 회전
            else:
                direction = (direction - 1) % 4  # 왼쪽 회전

# 예제 입력
n = 6
apples = [(2, 4), (1, 5), (4, 2)]  # 0-indexed
direction_changes = {
    3: 'D',
    15: 'L',
    17: 'D'
}

print(play_snake_game(n, apples, direction_changes))