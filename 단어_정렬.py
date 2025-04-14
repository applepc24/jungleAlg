n = int(input())
check_list = []

for _ in range(n):
    check_list.append(str(input()))

result = sorted(set(check_list), key = lambda x: (len(x), x))

for word in result:
    print(word)