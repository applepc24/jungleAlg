def is_acceptable(password):
    mo_words = set("aeiou")

    in_mo_words = False
    mo_words_count = 0
    ja_words_count = 0
    prev_char = ""

    for i,c in enumerate(password):
        if c in mo_words:
            in_mo_words = True
            mo_words_count += 1
            ja_words_count = 0
        else:
            mo_words_count = 0
            ja_words_count +=1
        
        if mo_words_count >= 3 or ja_words_count >=3:
            return False
        
        if i > 0:
            if c == prev_char and c not in ['e', 'o']:
                return False
        
        prev_char = c
    return in_mo_words


while True:
    word = input().strip()
    if word == "end":
        break
    if is_acceptable(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
