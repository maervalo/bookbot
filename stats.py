def get_num_words(text):
    new_list = text.split()
    return len(new_list)

def get_char_count(text):    
    new_dict = {}
    for char in text:
        char = char.lower()
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict
