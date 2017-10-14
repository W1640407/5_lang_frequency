import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, "r") as file_reader:
        file_content = file_reader.read()
    return file_content


def get_most_frequent_words(text):
    amount_of_words_to_print = 10
    return Counter(re.findall(r'\w+', text)).most_common(
        amount_of_words_to_print)


if __name__ == '__main__':
    filename = sys.argv[1]
    file_content = load_data(filename)
    frequent_words = get_most_frequent_words(file_content)
    print("10 most frequent words in file:")
    for i, (word, word_count) in enumerate(frequent_words, 1):
        print('{0:2}: {1}'.format(i, word))
