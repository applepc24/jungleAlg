

def find_char_at_index(index):
    length = 1
    total_chars = 0

    while True:
        count = 26 ** length
        chars_in_this_block = count * length
        if total_chars + chars_in_this_block > index:
            break
        total_chars += chars_in_this_block
        length += 1
    
    local_index = index -  total_chars
    string_index = local_index // length
    char_pos = local_index % length

    s = []
    for _ in range(length):
        s.append(chr(ord('A') + string_index % 26))
        string_index //= 26
    s.reverse()

    return s[char_pos]

index = int(input())
print(find_char_at_index(index))