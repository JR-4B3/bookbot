def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    lower = text.lower()
    count_dict = {}
    for char in lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def sorted_list(dict):
    dict_list = []

    for char, count in dict.items():
        dict_list.append({"char": char, "num": count})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
     

def sort_on(items):
    return items["num"]