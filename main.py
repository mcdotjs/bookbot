def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_book_word_counts(text)
    # print(text)
    print(f"words count is: {words_count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_counts(str):
    words = str.split()
    return len(words)


main()
