def main(): 
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    words_count = get_book_word_counts(text) 
    # print(text) print(f"words count is: {words_count}")   
    letters_count = get_letters_count(text)
    print(letters_count)

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

main()
