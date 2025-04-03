def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict


def get_report_data(chars_dict):
    chars_list = [{"char": key, "count": value}
                  for key, value in chars_dict.items()]
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    return chars_list


def report(path, text):
    words = get_num_words(text)
    chars_list = get_num_chars(text)
    chars_dict = get_report_data(chars_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in chars_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")
