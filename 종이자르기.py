garoSeroNum = list(map(int, input().split()))
N = int(input())

num_list = []
for _ in range(N):
    num_list.append(list(map(int, input().split())))

sero_cutnum_list = [0, garoSeroNum[1]]
garo_cutnum_list = [0, garoSeroNum[0]]

for cutarr in num_list:
    cut_type, cut_line = cutarr
    if cut_type == 0:
        sero_cutnum_list.append(cut_line)
    else:
        garo_cutnum_list.append(cut_line)

sero_cutnum_list.sort()
garo_cutnum_list.sort()

sero_lengths = []
for i in range(1, len(sero_cutnum_list)):
    length = sero_cutnum_list[i] - sero_cutnum_list[i-1]
    sero_lengths.append(length)

garo_lengths = []
for i in range(1, len(garo_cutnum_list)):
    length = garo_cutnum_list[i] - garo_cutnum_list[i-1]
    garo_lengths.append(length)

max_area = max(sero_lengths) * max(garo_lengths)
print(max_area)








