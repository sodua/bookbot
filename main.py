import sys
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(path_to_book))
    print("--------- Character Count -------")
    sorted_list = count_chars(get_book_text(path_to_book))

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
