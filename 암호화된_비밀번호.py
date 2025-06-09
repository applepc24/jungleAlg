from collections import Counter

T = int(input())

for _ in range(T):
    S = input().strip()
    P = input().strip()

    len_S = len(S)
    len_P = len(P)

    target = Counter(P)
    found = False

    for i in range(len_S - len_P + 1):
        window = S[i:i+len_P]
        if Counter(window) == target:
            found = True
            break
    
    if found:
        print("YES")
    else:
        print("NO")