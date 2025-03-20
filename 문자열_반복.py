n = int(input())

arr = []
for _ in range(n):
    arr.append(input().split())


for line in arr:
    r= int(line[0])
    s= line[1]
    for i in s:
        print(i*r, end = '')

    print()
    


        

