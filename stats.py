def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    y = text.lower()
    char_dict = {}
    for char in y:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict