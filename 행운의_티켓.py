s = input().strip()
n = len(s)
max_len = 0

for length in range(2, n+1, 2):
    for start in range(n - length + 1):
        mid = start + length //2
        left = s[start:mid]
        right = s[mid:start + length]

        left_sum = sum(map(int, left))
        right_sum = sum(map(int, right))

        if left_sum == right_sum:
            max_len = max(max_len, length)

print(max_len)

