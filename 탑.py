N = int(input())
heights = list(map(int, input().split()))

result = [0] * N
stack = []

for i in range(N-1, -1, -1):
    current_height = heights[i]

    while True:
        if not stack:
            break
        if current_height <= stack[-1][1]:
            break
        idx, h = stack.pop()
        result[idx] = i + 1
    
    stack.append((i, current_height))

print(' '.join(map(str, result)))