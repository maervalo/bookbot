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

def sort_chars(char_dict):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict_item):
    return dict_item["count"]


"""
Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
Each dictionary should have two key-value pairs: one for the character itself and one for that character's count.
Sort from greatest to least by the count.
The .sort() method will be helpful here (see the hint).
Import and call the function in main.py, and capture the result.
Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.
"""