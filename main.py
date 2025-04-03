def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    return len(text.split())


def main():
    text = get_book_text("./books/frankenstein.txt")
    words = count_words(text)
    print(f"{words} words found in the document")


main()
