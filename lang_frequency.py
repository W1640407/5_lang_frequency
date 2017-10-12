import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, "r") as file_reader:
        file_content = file_reader.read()
    return file_content


def get_most_frequent_words(text):
    words_list = text.split()
    words_amount_to_print = 10
    return Counter(words_list).most_common(words_amount_to_print)


if __name__ == '__main__':
    filename = sys.argv[1]
    file_content = load_data(filename)
    frequent_words = get_most_frequent_words(file_content)
    # Counter.most_common() returns array of pairs (a,b) where a - element, b - count, therefore calling pair[0] returns
    # element from this pair.
    print("10 наиболее часто встречающихся в тексте слов, по убыванию:")
    print([pair[0] for pair in frequent_words])
