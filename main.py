import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

def get_book_text(filepath):
    try:
          with open(filepath, 'r') as f:
               return f.read()
    except FileNotFoundError:
         print(f"Error: File not found - {filepath}")
         return None
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    if not book_text:
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    entire_content = get_book_text(book_path)
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