import math

a,b,v = map(int, input().split())

finish = (v-a) / (a-b)

day = math.ceil(finish) + 1

print(day)