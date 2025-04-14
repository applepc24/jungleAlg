x,y,w,h = map(int, input().split())

number = min(x, y ,w-x, h-y)
print (number)
