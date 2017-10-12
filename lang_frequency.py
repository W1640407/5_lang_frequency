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
    print("10 most frequent words in file:")
    for i in range(10):
        print(i+1, ': ', frequent_words[i][0])
