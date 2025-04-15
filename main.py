from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    entire_content = get_book_text("./books/frankenstein.txt")
    print("----------- Word Count ----------")
    number_of_words = get_num_words(entire_content)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    character_count = get_char_count(entire_content)
    #print(character_count)
    sorted_chars = sort_chars(character_count)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
main()