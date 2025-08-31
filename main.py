from stats import get_book_text, count_words, count_characters, dict_to_list

import sys


def report_on_book(file_path):
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    character_count = dict_to_list(count_characters(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in character_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")
    return None

def main():
    try:
        file_path = sys.argv[1]
        report_on_book(file_path)

    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()