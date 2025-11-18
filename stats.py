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
    dict_values = list(freq_list)
    list_of_sublists = []
    for dict2list in dict_values:
        list_of_sublists.append([value for value in dict2list.items()])
    for my_list in list_of_sublists:
        print(f"{my_list[0][1]}: {my_list[1][1]}")
