import sys
input = sys.stdin.readline

n = int(input())
spin = list(map(int, input().split()))

sticker = set()
removed = set()
max_stickers =0

for menu in spin:
    if menu in removed:
        continue
    if menu in sticker:
        sticker.remove(menu)
        removed.add(menu)
    else:
        sticker.add(menu)
        max_stickers = max(max_stickers, len(sticker))
        
print(max_stickers)