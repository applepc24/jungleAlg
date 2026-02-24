import sys
input = sys.stdin.readline

def lcp_len(a: str, b: str) -> int:
    m = min(len(a), len(b))
    i = 0
    while i < m and a[i] == b[i]:
        i += 1
    return i

n = int(input())
orig = []
words = []
for idx in range(n):
    w = input().strip()
    orig.append(w)
    words.append((w, idx))

# 1) 사전순 정렬
words.sort(key=lambda x: x[0])

# 2) 인접 단어들로 최대 LCP 길이 구하기
max_lcp = 0
for i in range(n - 1):
    w1, _ = words[i]
    w2, _ = words[i + 1]
    max_lcp = max(max_lcp, lcp_len(w1, w2))

# max_lcp == 0이면: 규칙상 S는 입력순 1등, T는 입력순 2등
if max_lcp == 0:
    print(orig[0])
    print(orig[1])
    sys.exit(0)

# 3) max_lcp 길이 prefix로 그룹핑해서, 각 prefix에서 가장 작은 idx 2개만 유지
groups = {}  # prefix -> (min1, min2)  (입력 인덱스)
INF = 10**9

for w, idx in words:
    pref = w[:max_lcp]
    if pref not in groups:
        groups[pref] = (idx, INF)
    else:
        a, b = groups[pref]
        if idx < a:
            groups[pref] = (idx, a)
        elif idx < b:
            groups[pref] = (a, idx)

# 4) 전체 그룹 중 (S idx, T idx) 가장 작은 쌍 선택
best_s, best_t = INF, INF
for a, b in groups.values():
    if b == INF:
        continue  # 2개 이상 단어가 없는 prefix
    if (a < best_s) or (a == best_s and b < best_t):
        best_s, best_t = a, b

print(orig[best_s])
print(orig[best_t])