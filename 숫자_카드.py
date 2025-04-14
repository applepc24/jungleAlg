import sys

input = sys.stdin.readline

N = int(input())
card_arr = list(map(int, input().split()))
M = int(input())
bigyo_arr = list(map(int, input().split()))


card_arr = set(card_arr)

result = []

for num in bigyo_arr:
  if num in card_arr:
    result.append('1')
  else:
    result.append('0')

print(' '.join(result))


