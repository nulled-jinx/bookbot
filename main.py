from stats import get_num_words


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    words = get_num_words(text)
    print(f"{words} words found in the document")


main()
