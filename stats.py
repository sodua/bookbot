def sort_on(items):
    return items["num"]

def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_chars(book_text):
    book_text = book_text.lower()
    freq_dict = {}
    char_cnt = 0
    new_freq_dict = {}
    for char in book_text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    for char, num in freq_dict.items():
        new_freq_dict[char] = {
                "char": char,
                "num": num
                }
    dict_values = new_freq_dict.values()
    freq_list = list(dict_values)
    freq_list.sort(reverse=True, key=sort_on)
    print(freq_list)
