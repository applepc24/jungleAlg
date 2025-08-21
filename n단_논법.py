def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    word_map = {}
    idx = 0
    MAX = 400
    adj = [[False]*MAX for _ in range(MAX)]

    def get_index(word):
        nonlocal idx
        if word not in word_map:
            word_map[word] = idx
            idx += 1
        return word_map[word]

    # 관계 입력 처리
    for i in range(1, n+1):
        a, _, b = data[i].split()
        u = get_index(a)
        v = get_index(b)
        adj[u][v] = True

    
    m = int(data[n+1])
    start_idx = n + 2

    # Floyd-Warshall 알고리즘
    for k in range(idx):
        for i in range(idx):
            for j in range(idx):
                if adj[i][k] and adj[k][j]:
                    adj[i][j] = True

    for i in range(start_idx, start_idx + m):
        a, _, b = data[i].split()
        if a in word_map and b in word_map and adj[word_map[a]][word_map[b]]:
            print("T")
        else:
            print("F")
solve()