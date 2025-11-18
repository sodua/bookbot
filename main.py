from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text("./books/frankenstein.txt"))
    print("--------- Character Count -------")
    sorted_list = count_chars(get_book_text("./books/frankenstein.txt"))

main()
