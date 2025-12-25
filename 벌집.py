import sys
input = sys.stdin.readline

N = int(input())

layer = 1
end =1

while N > end:
    end += 6*layer
    layer += 1

print(layer)