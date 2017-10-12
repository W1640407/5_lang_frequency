from collections import Counter


def load_data(filepath):
    file_reader = open(filepath, "r")
    file_content = file_reader.read()
    file_reader.close()
    return file_content


def get_most_frequent_words(text):
    words_list = str.split(text)
    words_to_print = 10
    return Counter(words_list).most_common(words_to_print)


if __name__ == '__main__':
    filename = input()
    file_content = load_data(filename)
    frequent_words = get_most_frequent_words(file_content)
    print([word[0] for word in frequent_words])
