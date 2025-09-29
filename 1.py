import sys

T = sys.stdin.readlines()

for line in T:
    n = line.strip()
    if not n:
        continue
    if n == "0":
        break
    n = int(n)
    
    rem = 0
    for L in range(1, n + 1):
        rem = (rem * 10 + 1) % n
        if rem == 0:
            print(L)
            break
            
