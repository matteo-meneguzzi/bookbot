def main(): 
    book_path = "books/frankenstein.txt"
    file_content = get_book_text(book_path)
    num_words = count_words(file_content)
    tot_char = count_single_char(file_content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document" + "\n")  # Adding a newline
    print_each_char_total(dict(sort_dict_value(tot_char)))
    print("--- End report ---")

def get_book_text(p):
    with open(p) as f:
        return f.read()

def count_words(text):
    word_count = len(text.split())
    return word_count 

def count_single_char(text):
    char_count = {}
    cleaned_string = ''.join(char for char in text if char.isalpha())
    for i in cleaned_string:
        lower_char = i.lower()
        if lower_char in char_count.keys():
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count
    #suggestion
    """ for i in cleaned_string:
        lower_char = i.lower()
        char_count[lower_char] = char_count.get(lower_char, 0) + 1
    return char_count """

    
def print_each_char_total(char_total):
    for key, value in char_total.items():
        print(f"The '{key}' character was found {value} times")
        
def sort_dict_value(dict):
    return sorted(dict.items(), key=lambda x:x[1], reverse=True)

main()