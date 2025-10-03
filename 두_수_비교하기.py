a, b = map(int, input().split())

s = (a>b) - (a<b)
print({-1: '<', 0: '==', 1: '>'} [s])