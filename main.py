from stats import report


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    report(path, text)


main()
