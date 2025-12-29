import sys
input = sys.stdin.readline

n = int(input())
channels = [input().strip() for _ in range(n)]

pos = 0
ans = []

def press1():
    global pos
    if pos < n - 1:
        pos += 1
    ans.append('1')

def press4():
    global pos, channels
    if pos > 0:
        channels[pos], channels[pos -1] = channels[pos-1], channels[pos]
        pos -= 1
    ans.append('4')

k1 = channels.index('KBS1')
for _ in range(k1):
    press1()
while pos > 0:
    press4()

k2 = channels.index('KBS2')
for _ in range(k2):
    press1()
while pos > 1:
    press4()

print(''.join(ans))