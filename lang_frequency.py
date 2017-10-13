import re
import sys
from collections import Counter

WORDS_AMOUNT_TO_PRINT = 10


def load_data(filepath):
    with open(filepath, "r") as file_reader:
        file_content = file_reader.read()
    return file_content


def get_most_frequent_words(text):
    return Counter(re.findall(r'\w+', text)).most_common(WORDS_AMOUNT_TO_PRINT)


if __name__ == '__main__':
    filename = sys.argv[1]
    file_content = load_data(filename)
    frequent_words = get_most_frequent_words(file_content)
    print("10 most frequent words in file:")
    for i, pair in enumerate(frequent_words):
        print('{0:2}: {1}'.format(i+1, pair[0]))
