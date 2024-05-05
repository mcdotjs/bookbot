def main(): 
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    words_count = get_book_word_counts(text) 
    print("--- Begin report of books/frankenstein.txt ---")

    letters_count = get_letters_count(text)
    print(f"{words_count} words found in the document")

    letters = make_list_of_dictionaries(letters_count)
    letters.sort(reverse = True, key = sort_on)
    print_letters_nicely(letters)

    print("--End of report--")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_counts(str):
    words = str.split()
    return len(words)

def get_letters_count(text):
    letters_dictionary = {}
    for letter in text:
        letter = letter.lower()
        letter_exist = letters_dictionary.get(letter)
        if letter_exist:
            letters_dictionary[letter] += 1
        else:
            letters_dictionary[letter] = 1
    return letters_dictionary

def make_list_of_dictionaries(dict):
    list = []
    for val in dict:
        list.append({"name":val, "num" : dict[val]})
    return list

def sort_on(dict):
    return dict["num"]

def print_letters_nicely(list):
    for item in list:
        print(f"The '{item["name"]}' character was found '{item["num"]}' times")

main()
