import sys
input = sys.stdin.readline
n = int(input())
base_word = input().strip()

def count_letter(w :str):
    cnt = [0] * 26
    for ch in w:
        cnt[ord(ch) - ord('A')] += 1
    return cnt

base = count_letter(base_word)

ans = 0
for _ in range(n-1):
    w = input().strip()
    cnt = count_letter(w)

    diff_sum = 0
    for i in range(26):
        diff_sum += abs(cnt[i] - base[i])
    
    len_diff = len(w) - len(base_word)

    if diff_sum == 0:
        ans += 1
    elif (len_diff == 1 or len_diff == -1) and diff_sum == 1:
        ans += 1
    elif len_diff == 0 and diff_sum == 2:
        ans += 1

print(ans)


