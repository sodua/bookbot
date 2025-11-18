from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    get_num_words(get_book_text("./books/frankenstein.txt"))
    count_chars(get_book_text("./books/frankenstein.txt"))
main()
