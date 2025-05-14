d, k = map(int, input().split())

fibo = [0] * (d+1)
fibo[1] = 1
fibo[2] = 1

for i in range(3, d+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

A = fibo[d - 2]
B = fibo[d -1]


for x in range(1, k+1):
    if(k - A * x) % B == 0:
        y = (k - A * x) // B
        if y >= 1:
            print(x)
            print(y)
            break