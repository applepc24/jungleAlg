num = int(input())
original = num
count = 0

while True:
    a = num // 10 + num% 10
    num = (num % 10) * 10 + a%10
    count += 1
    
    if num == original:
        break

print(count)

