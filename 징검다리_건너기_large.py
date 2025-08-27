from collections import deque

def can_reach(K, A):
    N = len(A)
    visited = [False] * N
    visited[0] = True
    queue = deque([0])

    while queue:
        curr = queue.popleft()
        for next in range(curr + 1, N):
            cost = (next - curr) * (1 + abs(A[curr] - A[next]))
            if cost <= K and not visited[next]:
                visited[next] = True
                queue.append(next)
    return visited[N -1]

def find_min_K(N, A):
    lo, hi = 0, 10**9
    answer = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_reach(mid, A):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer

N = int(input())
A = list(map(int, input().split()))
print(find_min_K(N, A))