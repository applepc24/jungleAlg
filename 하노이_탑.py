n = int(input())

print(2 ** n - 1)

def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
        return
    
    hanoi(n - 1, x, z, y)
    print(x, z) 
    hanoi(n - 1, y, x, z)  

if n <= 20:
    hanoi(n, 1, 2, 3)