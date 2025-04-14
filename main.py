from stats import get_num_words
from stats import get_char_count

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
    print(character_count)
# Expected to see keys like {'h': 1, 'e': 1, 'l': 3, ',', 1, ' ': 1, 'w': 1, 'o': 2, 'r': 1, 'd': 1, '!': 1}
main()