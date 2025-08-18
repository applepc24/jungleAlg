index = int(input())

def Letters(index):
    length = 1
    total_char = 0

    while True:
        count = 26 ** length
        char_in_this_block = count * length
        if total_char + char_in_this_block > index:
            break
        total_char += char_in_this_block
        length += 1

    local_index = index - total_char
    string_index = local_index // length
    char_pos = local_index % length

    s = []
    for _ in range(length):
        s.append(chr(ord('A') + string_index % 26))
        string_index //= 26
    s.reverse()

    return s[char_pos]

print(Letters(index))