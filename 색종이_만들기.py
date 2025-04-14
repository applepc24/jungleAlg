n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

blue_count = 0
white_count = 0

def cut(n, row_start, col_start):

    global blue_count , white_count
    base_color = arr[row_start][col_start]

    for i in range(row_start, row_start +n ):
        for j in range(col_start, col_start + n):
            if arr[i][j] != base_color:
                cut(n//2 , row_start, col_start)
                cut(n//2, row_start, col_start + n//2)
                cut(n//2, row_start + n // 2, col_start)
                cut(n//2, row_start + n // 2, col_start + n // 2)
                return
    if base_color == 1:
        blue_count += 1
    else:
        white_count +=1

cut(n, 0, 0)

print(white_count)
print(blue_count)




    
