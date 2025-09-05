import sys
input = sys.stdin.readline

vowels = set("aeiou")

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

word_mask = [0] * N
lists = [[] for _ in range(26)]

for i, w in enumerate(words):
    mask = 0
    seen = set()
    for ch in w:
        if ch in vowels:
            continue
        if ch not in seen:
            seen.add(ch)
            bit = ord(ch) - 97
            mask |= (1 << bit)
            lists[bit].append(i)
    word_mask[i] = mask

U = 0
known_total = N

result = []
for _ in range(M):
    o, x = input().split()
    bit = ord(x) - 97
    if x in vowels:
        result.append(str(known_total))
        continue
    if o == '1':
        if(U & (1 << bit)) == 0:
            for i in lists[bit]:
                if (word_mask[i] & U) == 0:
                    known_total -= 1
            U |= (1 << bit)
    else:
        if (U & (1 << bit)) != 0:
            U &= ~(1 << bit)
            for i in lists[bit]:
                if (word_mask[i] & U) == 0:
                    known_total +=1
    result.append(str(known_total))

print("\n".join(result))