def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content


def count_words(text):
    return len(text.split())


def count_characters(text):
    lower_text = text.lower()
    letter_dict = {}
    for c in lower_text:
        if c not in letter_dict.keys():
            letter_dict[c] = 1

        else:
            letter_dict[c] += 1

    return letter_dict

def dict_to_list(input_dict):
    def sort_on(items):
        return items["num"]
    
    result_list = []
    for i in input_dict:
        result_list.append({"char": i, "num": input_dict[i]})

    result_list.sort(reverse = True, key=sort_on)
    return result_list